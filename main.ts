// Copies the front-page image for Tuesday 24 November 2026 into the
// grader's output directory, byte for byte, every run. Fails loudly
// instead of writing nothing if the image is missing, and logs the
// copied size so a silent short copy can never pass unnoticed.
import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(here, "entry.png");
const dst = join(outDir, "entry.png");

if (!existsSync(src)) {
  throw new Error(`entry.png not found next to main.ts: ${src}`);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(src, dst);
const bytes = statSync(dst).size;
if (bytes !== statSync(src).size || bytes === 0) {
  throw new Error(`entry.png copy mismatch: wrote ${bytes} bytes`);
}
console.log(`wrote ${dst} (${bytes} bytes)`);
