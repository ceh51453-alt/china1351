// Douglas-Peucker line simplification + GeoJSON optimizer
// Reduces 2.3M coordinate points to ~80-120K while preserving shape

const fs = require('fs');

// Read the GeoJSON
const raw = fs.readFileSync('china_1351.js', 'utf8');
const jsonStr = raw.replace(/^[^{]*/, '').replace(/;?\s*$/, '');
const geo = JSON.parse(jsonStr);
const varName = raw.match(/^(const|var|let)\s+(\w+)/);
const prefix = varName ? `${varName[1]} ${varName[2]} = ` : 'const CHINA_1351 = ';

// Douglas-Peucker algorithm
function sqDist(p1, p2) {
  const dx = p1[0] - p2[0], dy = p1[1] - p2[1];
  return dx * dx + dy * dy;
}

function sqSegDist(p, p1, p2) {
  let x = p1[0], y = p1[1];
  let dx = p2[0] - x, dy = p2[1] - y;
  if (dx !== 0 || dy !== 0) {
    const t = ((p[0] - x) * dx + (p[1] - y) * dy) / (dx * dx + dy * dy);
    if (t > 1) { x = p2[0]; y = p2[1]; }
    else if (t > 0) { x += dx * t; y += dy * t; }
  }
  dx = p[0] - x; dy = p[1] - y;
  return dx * dx + dy * dy;
}

function simplifyDP(points, sqTolerance) {
  const len = points.length;
  if (len <= 2) return points;
  
  const markers = new Uint8Array(len);
  markers[0] = markers[len - 1] = 1;
  
  const stack = [[0, len - 1]];
  
  while (stack.length) {
    const [first, last] = stack.pop();
    let maxSqDist = 0, index = 0;
    
    for (let i = first + 1; i < last; i++) {
      const d = sqSegDist(points[i], points[first], points[last]);
      if (d > maxSqDist) { maxSqDist = d; index = i; }
    }
    
    if (maxSqDist > sqTolerance) {
      markers[index] = 1;
      if (first + 1 < index) stack.push([first, index]);
      if (index + 1 < last) stack.push([index, last]);
    }
  }
  
  return points.filter((_, i) => markers[i]);
}

function simplifyRing(ring, sqTolerance) {
  if (ring.length <= 4) return ring;
  const simplified = simplifyDP(ring, sqTolerance);
  // Ensure ring closure
  if (simplified.length >= 3) {
    const first = simplified[0], last = simplified[simplified.length - 1];
    if (first[0] !== last[0] || first[1] !== last[1]) {
      simplified.push([...first]);
    }
  }
  return simplified.length >= 4 ? simplified : ring;
}

// sqTolerance values — these are SQUARED distances in degrees
// 0.000001 = 0.001° ≈ 100m detail preservation
// 0.0000005 = high detail
function getToleranceForFeature(f) {
  const type = f.properties.TYPE;
  const name = f.properties.NAME || '';
  
  // Provinces: can be more aggressive
  if (type === 'province') return 0.0000015;
  
  // Large empires (Yuan, Chagatai, Tibet): moderate
  if (name.includes('Nguyên') || name.includes('Yuan') || 
      name.includes('Sat') || name.includes('Tây Tạng')) return 0.000001;
  
  // Small countries: preserve more detail
  return 0.0000008;
}

// Process
let beforeTotal = 0, afterTotal = 0;

function processCoords(coords, type, tolerance) {
  if (type === 'Polygon') {
    return coords.map(ring => {
      beforeTotal += ring.length;
      const simplified = simplifyRing(ring, tolerance);
      afterTotal += simplified.length;
      return simplified;
    });
  } else if (type === 'MultiPolygon') {
    return coords.map(polygon => 
      polygon.map(ring => {
        beforeTotal += ring.length;
        const simplified = simplifyRing(ring, tolerance);
        afterTotal += simplified.length;
        return simplified;
      })
    );
  }
  return coords;
}

// Round coordinates to 2 decimal places to save file size
function roundCoords(coords) {
  if (typeof coords[0] === 'number') {
    return [Math.round(coords[0] * 1000) / 1000, Math.round(coords[1] * 1000) / 1000];
  }
  return coords.map(roundCoords);
}

geo.features.forEach(f => {
  const tol = getToleranceForFeature(f);
  f.geometry.coordinates = processCoords(f.geometry.coordinates, f.geometry.type, tol);
  f.geometry.coordinates = roundCoords(f.geometry.coordinates);
});

console.log(`Before: ${beforeTotal.toLocaleString()} points`);
console.log(`After:  ${afterTotal.toLocaleString()} points`);
console.log(`Reduction: ${((1 - afterTotal / beforeTotal) * 100).toFixed(1)}%`);

// Backup original
fs.copyFileSync('china_1351.js', 'china_1351_full.js');
console.log('Backed up original to china_1351_full.js');

// Write optimized
const output = prefix + JSON.stringify(geo) + ';';
fs.writeFileSync('china_1351.js', output, 'utf8');

const newSize = fs.statSync('china_1351.js').size;
console.log(`New file size: ${(newSize / 1024 / 1024).toFixed(1)} MB`);
