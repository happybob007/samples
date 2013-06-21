  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>samples/python/Sheet_Structure/Sheet_Structure.md at master · pollackaaron/samples</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/modules/logos_page/Octocat.png">
    <link rel="assets" href="https://a248.e.akamai.net/assets.github.com/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="3860524" name="octolytics-actor-id" /><meta content="pollackaaron" name="octolytics-actor-login" /><meta content="2a71cfc52813767cfb10b2a057f8a96d1730105e376364b289d59e74a41ce8e2" name="octolytics-actor-hash" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="rHykMt4R6reFn1YIy6EnII+pWXJqcxVvxFU9j27AxBA=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-52c7f5d250c57ca1380f2a5703d96d015d5eb533.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-58b10e96bcdc3e0d5ea328ffcd01e36e2e8fd07e.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-4c434fa1705bf526e191eec0cd8fab1a5ce3e326.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-c9ee6873d0b9bc74d5f353bd006a81aa3efc29b3.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="9a05a1423af26d07af36db19fa49a2c8">

        <link data-pjax-transient rel='permalink' href='/pollackaaron/samples/blob/085c852ec60e4b8009d353d994022573ff23345f/python/Sheet_Structure/Sheet_Structure.md'>
    <meta property="og:title" content="samples"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/pollackaaron/samples"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/90491c7535daa9d83863e7f601d1059a?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="samples - Some sample applications in various languages demonstrating the use of the Smartsheet API."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="pollackaaron/samples"/>

    <meta name="description" content="samples - Some sample applications in various languages demonstrating the use of the Smartsheet API." />


    <meta content="3860524" name="octolytics-dimension-user_id" /><meta content="pollackaaron" name="octolytics-dimension-user_login" /><meta content="10066097" name="octolytics-dimension-repository_id" /><meta content="pollackaaron/samples" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="10062048" name="octolytics-dimension-repository_parent_id" /><meta content="smartsheet-platform/samples" name="octolytics-dimension-repository_parent_nwo" /><meta content="10062048" name="octolytics-dimension-repository_network_root_id" /><meta content="smartsheet-platform/samples" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/pollackaaron/samples/commits/master.atom" rel="alternate" title="Recent Commits to samples:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob macintosh vis-public fork env-production  ">
    <div id="wrapper">

      
      
      

      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    <div class="divider-vertical"></div>

    
  <a href="/notifications" class="notification-indicator tooltipped downwards" title="You have unread notifications">
    <span class="mail-status unread"></span>
  </a>
  <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    data-username="pollackaaron"
      data-repo="pollackaaron/samples"
      data-branch="master"
      data-sha="969a49c54113a91451f26aee4571af2aee34dced"
  >

    <input type="hidden" name="nwo" value="pollackaaron/samples" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
            <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    

  

    <ul id="user-links">
      <li>
        <a href="/pollackaaron" class="name">
          <img height="20" src="https://secure.gravatar.com/avatar/90491c7535daa9d83863e7f601d1059a?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /> pollackaaron
        </a>
      </li>

        <li>
          <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo">
            <span class="octicon octicon-repo-create"></span>
          </a>
        </li>

        <li>
          <a href="/settings/profile" id="account_settings"
            class="tooltipped downwards"
            title="Account settings ">
            <span class="octicon octicon-tools"></span>
          </a>
        </li>
        <li>
          <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out">
            <span class="octicon octicon-log-out"></span>
          </a>
        </li>

    </ul>


<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-list-unordered"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="pollackaaron/samples">This repository</span>
    </li>
    <li>
      <a href="/pollackaaron/samples/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
      <li>
        <a href="/pollackaaron/samples/settings/collaboration"><span class="octicon octicon-person-add"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

      




            <div class="global-notices">
      <div class="flash-global">
        <div class="container">
            <a href="/users/pollackaaron/enable_repository_next?nwo=pollackaaron%2Fsamples" class="button minibutton flash-action blue" data-method="post">Enable Repository Next</a>

            <h2>Hey there, would you like to enable our new repository design?</h2>
            <p>We&rsquo;ve been working hard making a <a href="https://github.com/blog/1529-repository-next">faster, better repository experience</a> and we&rsquo;d love to share it with you.</p>
        </div>
      </div>
    </div>
    <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">

    <li class="nspr">
      <a href="/pollackaaron/samples/pull/new/master" class="button minibutton btn-pull-request" icon_class="octicon-git-pull-request"><span class="octicon octicon-git-pull-request"></span>Pull Request</a>
    </li>

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="rHykMt4R6reFn1YIy6EnII+pWXJqcxVvxFU9j27AxBA=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="10066097" />

    <div class="select-menu js-menu-container js-select-menu">
      <span class="minibutton select-menu-button  js-menu-target">
        <span class="js-select-button">
          <span class="octicon octicon-eye-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

    <li class="js-toggler-container js-social-container starring-container ">
      <a href="/pollackaaron/samples/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star-delete"></span>
        <span class="text">Unstar</span>
      </a>
      <a href="/pollackaaron/samples/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star"></span>
        <span class="text">Star</span>
      </a>
      <a class="social-count js-social-count" href="/pollackaaron/samples/stargazers">0</a>
    </li>

        <li>
          <a href="/pollackaaron/samples/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="facebox nofollow">
            <span class="octicon octicon-git-branch-create"></span>
            <span class="text">Fork</span>
          </a>
          <a href="/pollackaaron/samples/network" class="social-count">2</a>
        </li>


</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-octicon octicon-repo-forked"></span>
                <span class="author vcard">
                  <a href="/pollackaaron" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">pollackaaron</span>
                  </a></span> /
                <strong><a href="/pollackaaron/samples" class="js-current-repository">samples</a></strong>
                  <span class="fork-flag">
                    <span class="text">forked from <a href="/smartsheet-platform/samples">smartsheet-platform/samples</a></span>
                  </span>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/pollackaaron/samples/pulse" class="js-selected-navigation-item " data-selected-links="pulse /pollackaaron/samples/pulse" rel="nofollow"><span class="octicon octicon-pulse"></span></a></li>
    <li><a href="/pollackaaron/samples" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /pollackaaron/samples">Code</a></li>
    <li><a href="/pollackaaron/samples/network" class="js-selected-navigation-item " data-selected-links="repo_network /pollackaaron/samples/network">Network</a></li>
    <li><a href="/pollackaaron/samples/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /pollackaaron/samples/pulls">Pull Requests <span class='counter'>0</span></a></li>


      <li><a href="/pollackaaron/samples/wiki" class="js-selected-navigation-item " data-selected-links="repo_wiki /pollackaaron/samples/wiki">Wiki</a></li>


    <li><a href="/pollackaaron/samples/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /pollackaaron/samples/graphs">Graphs</a></li>

      <li>
        <a href="/pollackaaron/samples/settings">Settings</a>
      </li>

  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/pollackaaron/samples/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /pollackaaron/samples/tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="octicon octicon-git-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/pollackaaron/samples/blob/master/python/Sheet_Structure/Sheet_Structure.md" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <form accept-charset="UTF-8" action="/pollackaaron/samples/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="rHykMt4R6reFn1YIy6EnII+pWXJqcxVvxFU9j27AxBA=" /></div>

                <span class="octicon octicon-git-branch-create select-menu-item-icon"></span>
                <div class="select-menu-item-text">
                  <h4>Create branch: <span class="js-new-item-name"></span></h4>
                  <span class="description">from ‘master’</span>
                </div>
                <input type="hidden" name="name" id="name" class="js-new-item-value">
                <input type="hidden" name="branch" id="branch" value="master" />
                <input type="hidden" name="path" id="branch" value="python/Sheet_Structure/Sheet_Structure.md" />
              </form> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/pollackaaron/samples" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /pollackaaron/samples">Files</a></li>
    <li><a href="/pollackaaron/samples/commits/master" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /pollackaaron/samples/commits/master">Commits</a></li>
    <li><a href="/pollackaaron/samples/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /pollackaaron/samples/branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:acbd0b36cd64f04e780cbce938d25d47 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:acbd0b36cd64f04e780cbce938d25d47 -->

<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <a href="/pollackaaron/samples/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>

        <div class="breadcrumb">
          <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/pollackaaron/samples" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">samples</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/pollackaaron/samples/tree/master/python" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">python</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/pollackaaron/samples/tree/master/python/Sheet_Structure" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">Sheet_Structure</span></a></span><span class="separator"> / </span><strong class="final-path">Sheet_Structure.md</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="python/Sheet_Structure/Sheet_Structure.md" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/pollackaaron/samples/contributors/master/python/Sheet_Structure/Sheet_Structure.md">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/pollackaaron/samples/blob/085c852ec60e4b8009d353d994022573ff23345f/python/Sheet_Structure/Sheet_Structure.md" data-title="samples/python/Sheet_Structure/Sheet_Structure.md at master · pollackaaron/samples · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>130 lines (95 sloc)</span>
                <span>7.579 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                        <a class="minibutton"
                           href="/pollackaaron/samples/edit/master/python/Sheet_Structure/Sheet_Structure.md"
                           data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
                  <a href="/pollackaaron/samples/raw/master/python/Sheet_Structure/Sheet_Structure.md" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/pollackaaron/samples/blame/master/python/Sheet_Structure/Sheet_Structure.md" class="button minibutton ">Blame</a>
                  <a href="/pollackaaron/samples/commits/master/python/Sheet_Structure/Sheet_Structure.md" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
              
  <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h2>
<a name="sheet-structure-documentation" class="anchor" href="#sheet-structure-documentation"><span class="octicon octicon-link"></span></a>Sheet Structure: Documentation</h2>

<h1></h1>

<h3>
<a name="this-walk-through-will-demonstrate-how-to-create-a-new-sheet-add-columns-and-rows-and-then-move-those-columns-and-rows-within-the-sheet-in-this-example-betty-is-having-a-bake-sale-well-use-the-data-from-her-bake-sale-to-help-illustrate-how-data-is-created-in-smartsheets-api" class="anchor" href="#this-walk-through-will-demonstrate-how-to-create-a-new-sheet-add-columns-and-rows-and-then-move-those-columns-and-rows-within-the-sheet-in-this-example-betty-is-having-a-bake-sale-well-use-the-data-from-her-bake-sale-to-help-illustrate-how-data-is-created-in-smartsheets-api"><span class="octicon octicon-link"></span></a>This walk through will demonstrate how to create a new sheet, add columns and rows, and then move those columns and rows within the sheet. In this example Betty is having a bake sale. We'll use the data from her bake sale to help illustrate how data is created in Smartsheet's API.</h3>

<hr><h2>
<a name="smartsheet-api" class="anchor" href="#smartsheet-api"><span class="octicon octicon-link"></span></a>Smartsheet API</h2>

<p>Familiarize yourself with the Smartsheet API. For information on the Smartsheet API, please see the <a href="http://smartsheet.com/developers">Smartsheet Developer Portal</a>.</p>

<h4>
<a name="libraries" class="anchor" href="#libraries"><span class="octicon octicon-link"></span></a>Libraries</h4>

<p>First import the standard libraries needed for HTTP requests and JSON parsing. When building a larger app in Python that makes frequent HTTP calls, I recommend using a library that will do caching and compression. <a href="https://code.google.com/p/httplib2/"> Httplib2 </a> is a great option for this.</p>

<pre><code>import urllib2
import json
</code></pre>

<h4>
<a name="helpers" class="anchor" href="#helpers"><span class="octicon octicon-link"></span></a>Helpers</h4>

<p>Store the base URL for all API calls to Smartsheet and ask the user for their access token.</p>

<pre><code>baseURL = "https://api.smartsheet.com/1.1"
token = "Please Put Access Token Here"
</code></pre>

<h4>
<a name="http-request-abstraction" class="anchor" href="#http-request-abstraction"><span class="octicon octicon-link"></span></a>HTTP Request Abstraction</h4>

<p>Create a class in Python that allows you to abstract the HTTP calls made throughout the script. Notice that you'll only need to specify the call method when using 'PUT.' urllib2 will automatically use 'GET' if no data is specified and a 'POST' if data is included. When using the 'PUT' method, pass it in as an argument when using the <code> _raw_request </code> method.</p>

<pre><code>class SmartsheetAPI(object):
    """Template for making calls to the Smartsheet API"""
    def __init__(self,url,token):
        self.baseURL = url
        self.token = " Bearer " + str(token)

    def _raw_request(self, url, extra_header = None, data = None, method = None):
        request_url = self.baseURL + url
        req = urllib2.Request(request_url)
        req.add_header("Authorization", self.token)

        if extra_header:
            req.add_header(extra_header[0], extra_header[1])
        if data:
            req.add_data(data)
        if method:
            if method == 'PUT':
                req.get_method = lambda: 'PUT'

        self.resp = urllib2.urlopen(req).read()
        return self.resp
</code></pre>

<hr><h4>
<a name="create-a-sheet" class="anchor" href="#create-a-sheet"><span class="octicon octicon-link"></span></a>Create a Sheet</h4>

<p>Betty is running a fundraising bake sale and needs to track her project status and inventory.  First, she needs to set up her project dashboard by creating a sheet with all the columns required to track the key attributes:  </p>

<pre><code>columns = [{"title":"Baked Good","primary":True, "type":"TEXT_NUMBER"},
           {"title":"Baker", "type":"CONTACT_LIST"},
           {"title":"Price Per Item", "type":"TEXT_NUMBER"},
           {"title":"Gluten Free?", "type":"CHECKBOX", "symbol":"FLAG"},
           {"title":"Status", "type":"PICKLIST", "options":["Started","Finished","Delivered"]}]

sheet = json.dumps({"name":"Betty's Bake Sale","columns":columns})

header = "Content-Type", " application/json"

createSheet = Call._raw_request('/sheets', header, sheet) # Create sheet
createSheetResp = json.loads(Call.resp)
sheet_id = createSheetResp['result']['id']
</code></pre>

<h4>
<a name="add-a-column" class="anchor" href="#add-a-column"><span class="octicon octicon-link"></span></a>Add a column</h4>

<p>Turns out, she missed an important column to track "Delivery Date" - so she adds it to the end of the sheet. </p>

<pre><code>column = json.dumps({"title":"Delivered", "type":"DATE", "index": 5})
insert_Column = Call._raw_request('/sheet/{}/columns'.format(sheet_id), header, column)
</code></pre>

<h4>
<a name="add-some-rows" class="anchor" href="#add-some-rows"><span class="octicon octicon-link"></span></a>Add some rows</h4>

<p>Betty needs to figure out who is preparing what for the sale, and when the items are going to be ready.  She inserts several rows to track that information:</p>

<pre><code>column_info = json.loads(Call._raw_request('/sheet/{}/columns'.format(sheet_id), header))
row_Insert1 =  json.dumps({"toTop":True, "rows":[ {"cells": [ 
                                                {"columnId":column_info[0]['id'], "value":"Brownies"},
                                                {"columnId":column_info[1]['id'], "value":"julieanne@smartsheet.com","strict": False},
                                                {"columnId":column_info[2]['id'], "value":"$1", "strict":False},
                                                {"columnId":column_info[3]['id'], "value":True},
                                                {"columnId":column_info[4]['id'], "value":"Finished"},
                                                {"columnId":column_info[5]['id'], "value": "None", "strict":False}]
                                               },{"cells":[ {"columnId":column_info[0]['id'], "value":"Snickerdoodles"},
                                               ]}, 
                                               {"columnId":column_info[1]['id'], "value":"stevenelson@smartsheet.com","strict":False},
                                                {"columnId":column_info[2]['id'], "value":"$1", "strict":False},
                                                {"columnId":column_info[3]['id'], "value":False},
                                                {"columnId":column_info[4]['id'], "value":"Delivered"},
                                                {"columnId":column_info[5]['id'], "value":"2013-09-04"}
                                               ]}, …remaing rows here…          
                                                ] 
                         })
insert_Rows = Call._raw_request('/sheet/{}/rows'.format(sheet_id), header, row_Insert1)
</code></pre>

<h4>
<a name="move-rows" class="anchor" href="#move-rows"><span class="octicon octicon-link"></span></a>Move rows</h4>

<p>Ned Barnes, who is making Ginger Snaps, is often late.  Betty moves his cookies to the top of the list so that she can keep an eye on them:</p>

<pre><code>toTop = json.dumps({"toTop":True})
move_row_up = Call._raw_request('/row/{}'.format(rows[5]['id']), header, toTop, 'PUT')
</code></pre>

<p>Betty realizes that a few of the items have already been delivered.  It would be handy to see them all in one place, so Betty takes advantage of Smartsheet's row hierarchy feature. She creates a "Delivered" section and moves all the delivered items there, making them children of "Delivered" (using the <code>parentId</code> attribute) so that they appear indented.</p>

<p>As more people volunteer, Betty keeps adding new baked goods to the list as siblings of existing items (using the <code>siblingId</code>).</p>

<pre><code>asChild = json.dumps({"parentId":rowDelivered['result'][2]['id']})

SnickerDoodles = rows[1]['id']
ChocolateChip = rows[4]['id']

Snickerdoodles_Id = json.loads(moveSnickerdoodles)

asSibling = json.dumps({"siblingId":Snickerdoodles_Id['result'][0]['id']})
moveCCCookies = Call._raw_request('/row/{}'.format(ChocolateChip), header, asSibling, 'PUT') #column ID's instead of values                    
</code></pre>

<h4>
<a name="move-column" class="anchor" href="#move-column"><span class="octicon octicon-link"></span></a>Move column</h4>

<p>The bake sale list is coming together.  Looking at the sheet, Betty decides that the "Status" column ought to be moved up (to index 1)to make it easier to identify delinquent items:</p>

<pre><code>get_columns = json.loads(Call._raw_request('/sheet/{}/columns'.format(sheet_id)))

for columns in get_columns:
    if columns['title'] == 'Status': #Move 'Status' to column 2
        columnID = columns['id']
        location = json.dumps({"title":'Status', "index":1, "sheetId":sheet_id})
        move_column = Call._raw_request('/column/{}'.format(columnID), header, location, 'PUT')
</code></pre>

<p>Congratulations! Betty's Bake Sale was well planned and went off without a hitch. You've now completed the walkthrough for creating and manipulating data in a sheet. Please feel free to contact us at <a href="mailto:api@smartsheet.com">api@smartsheet.com</a> with any questions or suggestions.</p>

<p>The Smartsheet Platform team.</p></article>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;">
            <button type="submit" class="button">Go</button>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="/about">About us</a></dd>
        <dd><a href="/blog">Blog</a></dd>
        <dd><a href="/contact">Contact &amp; support</a></dd>
        <dd><a href="https://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="https://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="https://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="https://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="https://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.10566s from fe17.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>
    <ul id="legal">
        <li><a href="/site/terms">Terms of Service</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/pollackaaron/samples/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
    <span id='server_response_time' data-time='0.10610' data-host='fe17'></span>
    
  </body>
</html>

