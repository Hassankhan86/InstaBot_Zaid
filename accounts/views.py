import random
from random import randint
import csv, io
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
import keyboard
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.forms import PasswordChangeForm
from accounts.forms import AddAccount, AddComment
from accounts.models import Account, Comments, Profile
import time
from selenium import webdriver
from time import sleep
from django.contrib.auth.decorators import login_required
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.chrome.options import Options


# from selenium.common.exceptions import NoSuchElementException
@login_required(login_url='/accounts/login')
def createAccount(request):
    form = AddAccount()
    if request.method == 'POST':
        form = AddAccount(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:accountview')

    context = {'form': form}
    return render(request, 'accounts/addaccount.html', context)


def delete_all_accounts(request):
    Account.objects.all().delete()
    return accountview(request)


def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return home(request)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/changepassword.html', {
        'form': form
    })


@login_required(login_url='/accounts/login')
def updateaccount(request, id):
    acc = Account.objects.get(id=id)
    form = AddAccount(instance=acc)
    print(id)
    if request.method == 'POST':
        form = AddAccount(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect('accounts:accountview')

    context = {'form': form}
    return render(request, 'accounts/updateaccount.html', context)


@login_required(login_url='/accounts/login')
def accountview(request):
    acc = Account.objects.all()
    return render(request, 'accounts/accountsview.html', {'acc': acc})


@login_required(login_url='/accounts/login')
def deleteaccount(request, id):
    obj = get_object_or_404(Account, id=id)
    obj.delete()
    return accountview(request)


@login_required(login_url='/accounts/login')
def home(request):
    accounts = Account.objects.filter(status=1)
    maximum = len(accounts)
    return render(request, 'accounts/index.html', {'maximum': maximum})


@login_required(login_url='/accounts/login')
def addcomment(request):
    form = AddComment()
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:commentview')

    context = {'form': form}
    return render(request, 'accounts/addcomment.html', context)


@login_required(login_url='/accounts/login')
def updatecomment(request, id):
    acc = Comments.objects.get(id=id)
    form = AddComment(instance=acc)
    print(id)
    if request.method == 'POST':
        form = AddComment(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect('accounts:commentview')

    context = {'form': form}
    return render(request, 'accounts/updatecomment.html', context)


@login_required(login_url='/accounts/login')
def commentview(request):
    comment = Comments.objects.all()
    return render(request, 'accounts/commentview.html', {'comment': comment})


@login_required(login_url='/accounts/login')
def deletecomment(request, id):
    obj = get_object_or_404(Comments, id=id)
    obj.delete()
    return commentview(request)


def logout_views(request):
    if request.method == 'POST':
        print("-------------")
        logout(request)
        return render(request, 'accounts/newlogin.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)

            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            return redirect('accounts:abc')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/newlogin.html', {'form': form})


def reportview(request):
    return render(request, 'accounts/report.html')


def errormessage(request):
    return render(request, 'accounts/error_message.html')


@login_required(login_url='/accounts/login')
def instabotcode(request):
    # if request.method == 'POST':
    try:
        print('sss')

        like = request.POST.get('liked')
        comment = request.POST.get('commented')
        story = request.POST.get('storyview')
        follow = request.POST.get('followed')
        accounts_no = request.POST.get('account_number_tag')
        numb = int(accounts_no)
        print('sss')

        like_report = 0
        comment_report = 0
        story_report = 0
        follow_report = 0
        acc_search = []
        acc_username = []
        acc_password = []
        # comment_list = []
        # comment = Comments.objects.all()
        # print(comment)
        # print(comment_list)
        print('sss')
        accounts = Account.objects.filter(status =1)
        print(accounts)
        if request.POST:
            target = request.POST.get('example-tags')
            acc_search = target.split(',')
            print(acc_search)

            like = request.POST.get('liked')
            comment = request.POST.get('commented')
            story = request.POST.get('storyview')
            follow = request.POST.get('followed')
            # pro = Profile(follow=follow, comment=comment, like=like, story=story)
            print(like)
            print(comment)
            print(story)
            print(follow)
            # pro.save()

        maximum = len(accounts)
        print(maximum)

        # for com in Comments.objects.all():
        #     comment_list.append(com.title)
        #     print(comment_list)
        # print(com)

        # com.append

        # accounts.get(use)

        # clearButton = driver.execute_script(
        #     "return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
        # # click on the clear button now
        # clearButton.click()

        # driver.findElement(By.name("s")).sendKeys(Keys.F5);

        # print(driver.title)
        # time.sleep(5)

        print(accounts)
        for acc in accounts[:numb]:
            acc_username.append(acc.userid)
            acc_password.append(acc.password)

            # options.headless = True
            # options.add_argument('--disable-gpu')  # Last I checked this was necessary.

            options = Options()
            options.add_argument("window-size=1280,800")
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument('--disable-blink-features=AutomationControlled')

            # options = webdriver.ChromeOptions()

            # chromepath = "chromedriver.exe"  # Headless
            # driver = webdriver.Chrome(options=options)

            driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)
            print('----------------1')
            # chromepath = "chromedriver.exe"  # Headless
            # driver = webdriver.Chrome(executable_path=chromepath,)
            driver.minimize_window()

            driver.get("chrome://settings/clearBrowserData")
            sleep(3)
            clearButton = driver.execute_script(
                "return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
            # click on the clear button now
            clearButton.click()
            # actions = ActionChains(driver)
            # actions.send_keys(Keys.TAB * 7 + Keys.ENTER)
            # actions.perform()
            # keyboard.send("Enter")
            print('Cache Clear Successfully')
            # sleep(0)
            time.sleep(random.randint(1,2))
            # print(t)
            # driver.quit()
            print('----------------2')

            driver.get('https://www.instagram.com/')

            print('----------------3')
            # driver.execute_script("window.open('about:blank', 'tab4');")
            # driver.switch_to.window("tab2")
            # driver.get('http://bing.com')

            wait = WebDriverWait(driver, 10)
            print('----------------4')

            time.sleep(random.randint(1,2))
            # sleep(3)

            print('Webpage :' + driver.title)
            Username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")))
            Username.send_keys(acc.userid)
            print("Username :" + acc.userid)

            # sleep(1)

            Password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")))
            Password.send_keys(acc.password)
            print("Password : " + acc.password)

            # time.sleep(1)

            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=submit]'))).click()

            time.sleep(random.randint(2, 4))
            # time.sleep(5)

            # try:
            #
            #     notnow = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not Now")]'))).click()
            #     sleep(5)
            #     notti = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not Now")]'))).click()
            #     if notti.is_displayed():
            #         notti.click()
            #         sleep(5)
            #
            # except:
            #     print('Notification notnow in Not Appear')
            #     pass

            try:
                wrongpass = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@aria-atomic="true"]')))
                if wrongpass.is_displayed():
                    print("Sorry, your password was incorrect.")
                    # driver.refresh()

                    driver.quit()

                    acc.status = 0
                    acc.save()
                    print('Account status change to  0 ')
                    continue

            except:
                print('Login Successfully  with : ' + acc.userid)
                pass

            try:
                verifyacc = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div[1]/div/div[2]/button')))
                if verifyacc.is_displayed():
                    print('Verify Email - Switch to next account Successfully  : ' + acc.userid)
                    driver.quit()
                    # sleep(3)
                    # driver.get('https://www.instagram.com/')

                    acc.status = 0
                    acc.save()
                    print('Account status change to  0 ')
                    continue
            except:
                print('Login Successfully  with : ' + acc.userid)
                pass

            for search in range(len(acc_search)):
                time.sleep(random.randint(2, 4))
                # sleep(5)
                print('Search Pic Link : ' + acc_search[search])
                driver.get(acc_search[search])

                # Search = wait.until(EC.visibility_of_element_located(
                #     (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')))
                # Search.send_keys(acc_search[search])
                # sleep(10)
                # Profile_Open = wait.until(EC.element_to_be_clickable(
                #     (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')))
                # Profile_Open.click()
                # sleep(10)

                # sleep(0)

# <=-------------------=>
                if like == None:
                    pass
                else:
                    try:
                        print('------------------------')
                        time.sleep(random.randint(1, 3))
                        # sleep(3)
                        like_func(wait, driver)
                        like_report += 1
                        print('------------------------')
                    except:
                        # driver.quit()
                        print('Like Restricted')
                        print('Verify Your Account')

                        # acc.status = 0
                        # acc.save()
                        # print('Account status change to  0 ')
                        # follow_report -= 1
                        continue

                if comment == None:
                    pass
                else:
                    try:
                        print('------------------------')
                        sleep(3)
                        comment_report = comment_func(wait, driver, comment_report)
                        print(comment_report)
                        print('cccc')
                        # sleep(3)
                        print('-----------------------s-')

                    except:
                        # driver.quit()

                        print('Comment Restricted')
                        print('Verify Your Account')

                        # acc.status = 0
                        # acc.save()
                        # print('Account status change to  0 ')

                        continue


# <=-------------------=>
                try:
                    time.sleep(random.randint(3, 5))
                    profile = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 '/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a'))).click()
                # if profile.is_displayed():
                # profile.click()
                    time.sleep(random.randint(2, 3))
                except:
                    continue
# <=-------------------=>

                if story == None:
                    pass
                else:
                    try:
                        time.sleep(random.randint(1, 2))
                        # sleep(2)
                        print(story_report)
                        story_report = story_func(wait, driver, story_report)
                        print('sss')

                    except:
                        # driver.quit()
                        print('Story No Found ')
                        # print('Verify Your Account')
                        continue

                if follow == None:
                    pass
                else:
                    try:
                        print('------------------------')
                        # print(follow_report)
                        # follow_report += 2
                        # print(follow_report)
                        follow_report = follow_func(wait, driver, follow_report)

                        print('------------------------')
                        print('fff')
                        # follow_report += 1

                        # print(follow_report)
                        # story_report += 1
                    except:
                        # driver.quit()
                        print("Follow Already")

                    # acc = Account.objects.get()
                    # Account.objects.update(status=F('status')-1)


                # driver.get(acc_search[search])


            try:
                LogOutBtn = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img'))).click()
                time.sleep(random.randint(1, 2))
                # time.sleep(3)
                Logout = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div'))).click()

                time.sleep(random.randint(1, 2))
                # sleep(2)
                driver.quit()
                # sleep(4)
                print('Logout Successfully ')
                print('--------')
            except:
                driver.quit()
                print('Account Detected ')
                acc.status = 0
                acc.save()
                print('Account status change to  Not Verify ')
                continue

        # driver.quit()

        return render(request, 'accounts/report.html',
                      {'target': target, 'like_report': like_report, 'comment_report': comment_report,
                       'story_report': story_report, 'follow_report': follow_report})
    except:
        #     # return HttpResponse("Network problem")
        return render(request, 'accounts/error_message.html')


def follow_func(wait, driver, follow_report):
    fol_rep = follow_report

    print(fol_rep)
    time.sleep(random.randint(2, 3))
    # sleep(3)
    followButton = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Follow")]')))

    if (followButton.text != 'Following'):
        followButton.click()
        # time.sleep(2)
        print("Click oN  Follow Button")
        fol_rep += 1
        print(fol_rep)

        try:
            res = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"OK")]')))
            if res.is_displayed():
                print('Follow Restrict')
                fol_rep -= 1
                print(fol_rep)
        except:
            print('Follow Successfully')
            # follow_report -= 1

    else:
        print("You are already following this user")

    return fol_rep
    # return follow_report
    # if Follow.is_displayed():
    # print('Follow Successfully ')
    #     Follow.click()
    # follow_report += 1
    # try:
    #     cancel = wait.until(
    #             EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Cancel")]')))
    #     if cancel.is_displayed():
    #         cancel.click()
    #         print('Already Successfully  :' )
    # except:
    #     print('Follow Successfully ')
    #     pass
    #
    # time.sleep(5)
    # print('Follow Successfully  :' + acc_search[search])
    # follow_report += 1
    # follow_report += 1

    # except:
    #     # print('Already Follow :' + acc_search[search])
    #     pass
    #
    # return follow_report


def like_func(wait, driver):
    # sleep(5)
    like_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Like"]'))).click()
    # sleep(5)
    print('Pic Liked Successfully : ')
    # like_report += 1

    # if (like_button.text != 'Unlike'):
    #     like_button.click()
    #     time.sleep(2)
    #     print("Click oN  Follow Button")
    # # print('Already Liked Pic :')
    # else:
    #     print('Already Liked')

    # return a


def comment_func(wait, driver, comment_report):
    com_list = []
    for com in Comments.objects.all():
        com_list.append(com.title)
        print(com_list)

    # try:
    #     sleep(5)
    #     Post = WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"OK")]'))).click()
    #     print('Restricted Comment')
    # except:
    comm_rep = comment_report
    print(comm_rep)
    # sleep(5)

    before_comment = len(driver.find_elements_by_class_name('Mr508'))
    print(before_comment)

    time.sleep(random.randint(1, 3))
    # sleep(3)
    comment = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@aria-label="Add a comment…"]')))
    if comment.is_displayed():
        comment.click()
        # comment.send_keys(random.choice(com_list))
        # sleep(2)
        time.sleep(random.randint(1, 2))
    msg = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.XPATH,
         '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea'))).send_keys(
        random.choice(com_list))
    time.sleep(random.randint(1, 2))
    # sleep(2)

    Post = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Post")]'))).click()
    comm_rep += 1
    print(comm_rep)
    # pp = WebDriverWait(driver, 2).until(
    #         EC.element_to_be_clickable(By.XPATH, '//button[contains(text(),"Post")]'))).getText();
    sleep(10)

    # After_comment = len(wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Mr508'))))
    After_comment = len(driver.find_elements_by_class_name('Mr508'))
    print(After_comment)

    if After_comment > before_comment:
        # comment_report -=1
        print("Comment SuccessFully")
    else:
        comm_rep -= 1
        print("Comment After and Before")

    return comm_rep
    # print('Comment Successfully')
    # sleep(5)

    # comment_report += 1
    # print('Already Comment :' + acc_search[search])
    # else:
    #     print('NOOO ')
    #     pass

    # pass
    # sleep(5)


def story_func(wait, driver, story_report):
    fol_story = story_report


    # sleep(2)
    # print('333')
    try:
        Story = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_6q-tv'))).click()
        time.sleep(random.randint(3,4))
        # time.sleep(3)
        StoryClose = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[3]/button')))
        if StoryClose.is_displayed():
            StoryClose.click()
            print('Story1 Seen Successfully')
            fol_story += 1
            print(fol_story)

    except:
        # fol_story -= 1
        print(fol_story)
        print('Story Not Found')

    return fol_story
    # else::

    # except:
    #
    #     try:
    #         sleep(5)
    #         Storyp = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_6q-tv')))
    #         sleep(4)
    #         # print('ssssfff')
    #         if Storyp.is_displayed():
    #             Storyp.click()
    #             sleep(4)
    #             StoryClose = wait.until(
    #                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[3]/button'))).click()
    #             # if StoryClosep.is_displayed():
    #             #     StoryClosep.click()
    #             print('Story2 Seen Successfully : ')
    #             # story_report += 1
    #     # else:
    #     except:
    #         pass
    #         #     pass
    #         #     print('No story Found')
    #         print('Story Not Found')
    #     pass
    #     # sleep(5)

# @permission_required('admin')
