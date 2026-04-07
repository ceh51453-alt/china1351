class SpriteAnimator {
    constructor(canvasElement, imageUrl, cols = 2, rows = 2, fps = 4) {
        this.canvas = canvasElement;
        this.ctx = this.canvas.getContext('2d');
        this.cols = cols;
        this.rows = rows;
        this.fps = fps;
        
        this.image = new Image();
        this.image.src = imageUrl;
        this.isLoaded = false;
        
        this.currentFrame = 0;
        this.totalFrames = cols * rows;
        this.frameWidth = 0;
        this.frameHeight = 0;
        
        this.lastRenderTime = Date.now();
        this.animationId = null;

        // Content bounds (to trim empty space if needed, optional but good for learning)
        this.bounds = null;

        this.image.onload = () => {
            this.frameWidth = this.image.width / this.cols;
            this.frameHeight = this.image.height / this.rows;
            this.isLoaded = true;
            this.calculateContentBounds(); // Learn behavior
            this.play();
        };
    }

    calculateContentBounds() {
        this.bounds = { x: 0, y: 0, width: this.frameWidth, height: this.frameHeight };
        
        // Let's create a temporary canvas to get ImageData
        const tempCanvas = document.createElement('canvas');
        tempCanvas.width = this.frameWidth;
        tempCanvas.height = this.frameHeight;
        const tempCtx = tempCanvas.getContext('2d');
        
        // Draw first frame to temp canvas
        tempCtx.drawImage(this.image, 0, 0, this.frameWidth, this.frameHeight, 0, 0, this.frameWidth, this.frameHeight);
        const imageData = tempCtx.getImageData(0, 0, this.frameWidth, this.frameHeight);
        const data = imageData.data;
        
        let minX = this.frameWidth, minY = this.frameHeight, maxX = 0, maxY = 0;
        
        for (let y = 0; y < this.frameHeight; y++) {
            for (let x = 0; x < this.frameWidth; x++) {
                const index = (y * this.frameWidth + x) * 4;
                const r = data[index];
                const g = data[index + 1];
                const b = data[index + 2];
                // Since our image has a black background, detect non-black pixels
                if (r > 10 || g > 10 || b > 10) {
                    if (x < minX) minX = x;
                    if (x > maxX) maxX = x;
                    if (y < minY) minY = y;
                    if (y > maxY) maxY = y;
                }
            }
        }
        
        if (maxX >= minX && maxY >= minY) {
            // Padding
            const padding = 5;
            this.bounds = {
                x: Math.max(0, minX - padding),
                y: Math.max(0, minY - padding),
                width: Math.min(this.frameWidth - minX, maxX - minX + 1 + padding * 2),
                height: Math.min(this.frameHeight - minY, maxY - minY + 1 + padding * 2)
            };
        }
    }

    update() {
        if (!this.isLoaded) return;
        
        const now = Date.now();
        if (now - this.lastRenderTime >= 1000 / this.fps) {
            this.currentFrame = (this.currentFrame + 1) % this.totalFrames;
            this.lastRenderTime = now;
            this.render();
        }
        
        this.animationId = requestAnimationFrame(() => this.update());
    }

    render() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        const col = this.currentFrame % this.cols;
        const row = Math.floor(this.currentFrame / this.cols);
        
        const sourceX = col * this.frameWidth + this.bounds.x;
        const sourceY = row * this.frameHeight + this.bounds.y;
        
        // Optionally scale the sprite to fit the target canvas width/height
        const scaleX = this.canvas.width / this.bounds.width;
        const scaleY = this.canvas.height / this.bounds.height;
        const scale = Math.min(scaleX, scaleY);
        
        const drawWidth = this.bounds.width * scale;
        const drawHeight = this.bounds.height * scale;
        const drawX = (this.canvas.width - drawWidth) / 2;
        const drawY = (this.canvas.height - drawHeight) / 2;
        
        this.ctx.drawImage(
            this.image,
            sourceX, sourceY,
            this.bounds.width, this.bounds.height,
            drawX, drawY,
            drawWidth, drawHeight
        );
    }

    play() {
        if (!this.animationId) {
            this.lastRenderTime = Date.now();
            this.update();
        }
    }

    stop() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
    }

    destroy() {
        this.stop();
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}
