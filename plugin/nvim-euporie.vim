if !has('python3')
    echomsg ':python3 is not available, nvim-euporie will not be loaded.'
    finish
endif

python3 import nvim_euporie.euporie
python3 euporie = nvim_euporie.euporie.Euporie()

command! RunEuporie = python3 euporie.run()
