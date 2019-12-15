var gulp = require("gulp");

const css = () => {
  const sass = require("gulp-sass");
  const postCSS = require("gulp-postcss");
  const minify = require("gulp-csso");
  sass.compiler = require("node-sass");
  return gulp
    .src("assets/scss/styles.scss") //해당 위치에서 작업함
    .pipe(sass().on("error", sass.logError)) // sass로 pipe함
    .pipe(postCSS([require("tailwindcss"), require("autoprefixer")])) // postCss(tailwind 내용을 가져와 css로 만들어줌 )
    .pipe(minify()) // 작업이 끝나면 모든 아웃풋을 minify(사이즈 축소)함
    .pipe(gulp.dest("static/css")); // 여기까지 완성된 결과물은 static/css로 저장됨
};

exports.default = css;
