// news-image-20261120 entrypoint (Node 22, standard library only).
// The entry is the image entry.png beside this file. Copy it into the
// output directory the grader provides, unchanged, every run.
// The grader runs this twice and both runs must write identical bytes;
// a plain copy of a fixed file guarantees that.

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = new URL("./entry.png", import.meta.url);
copyFileSync(source, join(outDir, "entry.png"));
