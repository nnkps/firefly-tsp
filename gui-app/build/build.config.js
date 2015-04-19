'use strict';

//basic configuration object used by gulp tasks
module.exports = {
  port: 3000,
  tmp: 'build/tmp',
  dist: 'build/dist',
  base: 'app',
  tpl: 'app/modules/**/*.html',   
  mainScss: 'app/app.scss', 
  scss: 'app/**/*.scss', 
  js: [
    'app/modules/**/*.js',
    '!app/vendor/**/*.js',
    'app/**/*-spec.js',   //unit
    'app/test/e2e/**/*.js'  //e2e
  ],
  index: 'app/index.html',
  assets: 'app/assets/**',
  images: 'app/assets/images/**/*',
  banner: ['/**',
    ' * generator-cg-gas - Yeoman Generator for Enterprise Angular projects, with Gulp Angular Sass',
    ' * @version v3.3.4',
    ' * @link https://github.com/Lunatic83/generator-cg-gas',
    ' * @license ',
    ' */',
    ''
  ].join('\n')
};
