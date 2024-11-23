from pyocticons import octicon


def test_octicon():
    icon = octicon("alert", 24)

    assert (
        icon
        == """<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' class='octicon octicon-alert'><path d="M13 17.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Zm-.25-8.25a.75.75 0 0 0-1.5 0v4.5a.75.75 0 0 0 1.5 0v-4.5Z"></path><path d="M9.836 3.244c.963-1.665 3.365-1.665 4.328 0l8.967 15.504c.963 1.667-.24 3.752-2.165 3.752H3.034c-1.926 0-3.128-2.085-2.165-3.752Zm3.03.751a1.002 1.002 0 0 0-1.732 0L2.168 19.499A1.002 1.002 0 0 0 3.034 21h17.932a1.002 1.002 0 0 0 .866-1.5L12.866 3.994Z"></path></svg>"""
    )


def test_missing_octicon():
    icon = octicon("nonexistent", 24)

    assert icon is None


def test_custom_size():
    icon = octicon("alert", 48)

    assert icon is not None
    assert "width='48' height='48' viewBox='0 0 24 24'" in icon
