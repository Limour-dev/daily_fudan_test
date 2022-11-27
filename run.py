def main(image):
    try:
        from captcha_break_dddd import dddd
        for i in range(3):
            img = image
            result = dddd(img)
            if len(result) == 4:
                return result
    except:
            import traceback
            print(traceback.format_exc())
            
    return 'captcha_break by ttshitu'

if __name__ == "__main__":
    with open("01.jpg", 'rb') as f:
        image = f.read()
    print(main(image))
