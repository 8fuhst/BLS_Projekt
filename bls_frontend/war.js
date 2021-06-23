const zipper = require('zip-a-folder')
zipper.zip('dist/', 'BLS_Tool.war')
    .then(console.log('war file created successfully'))
    .catch(error => console.log(error))