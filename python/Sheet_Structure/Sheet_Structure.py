  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>samples/python/Sheet_Structure/Sheet_Structure.py at master · pollackaaron/samples</title>
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

        <link data-pjax-transient rel='permalink' href='/pollackaaron/samples/blob/085c852ec60e4b8009d353d994022573ff23345f/python/Sheet_Structure/Sheet_Structure.py'>
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
                  <a href="/pollackaaron/samples/blob/master/python/Sheet_Structure/Sheet_Structure.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
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
                <input type="hidden" name="path" id="branch" value="python/Sheet_Structure/Sheet_Structure.py" />
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
          


<!-- blob contrib key: blob_contributors:v21:58f634f4330095aa5805c31ca9f34775 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:58f634f4330095aa5805c31ca9f34775 -->

<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <a href="/pollackaaron/samples/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>

        <div class="breadcrumb">
          <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/pollackaaron/samples" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">samples</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/pollackaaron/samples/tree/master/python" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">python</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/pollackaaron/samples/tree/master/python/Sheet_Structure" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">Sheet_Structure</span></a></span><span class="separator"> / </span><strong class="final-path">Sheet_Structure.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="python/Sheet_Structure/Sheet_Structure.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/pollackaaron/samples/contributors/master/python/Sheet_Structure/Sheet_Structure.py">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/pollackaaron/samples/blob/085c852ec60e4b8009d353d994022573ff23345f/python/Sheet_Structure/Sheet_Structure.py" data-title="samples/python/Sheet_Structure/Sheet_Structure.py at master · pollackaaron/samples · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>204 lines (152 sloc)</span>
                <span>11.564 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                        <a class="minibutton"
                           href="/pollackaaron/samples/edit/master/python/Sheet_Structure/Sheet_Structure.py"
                           data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
                  <a href="/pollackaaron/samples/raw/master/python/Sheet_Structure/Sheet_Structure.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/pollackaaron/samples/blame/master/python/Sheet_Structure/Sheet_Structure.py" class="button minibutton ">Blame</a>
                  <a href="/pollackaaron/samples/commits/master/python/Sheet_Structure/Sheet_Structure.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><span class="c">#</span></div><div class='line' id='LC3'><span class="c">#   Copyright 2013 Smartsheet</span></div><div class='line' id='LC4'><span class="c">#</span></div><div class='line' id='LC5'><span class="c">#   Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span></div><div class='line' id='LC6'><span class="c">#   you may not use this file except in compliance with the License.</span></div><div class='line' id='LC7'><span class="c">#   You may obtain a copy of the License at</span></div><div class='line' id='LC8'><span class="c">#</span></div><div class='line' id='LC9'><span class="c">#       http://www.apache.org/licenses/LICENSE-2.0</span></div><div class='line' id='LC10'><span class="c">#</span></div><div class='line' id='LC11'><span class="c">#   Unless required by applicable law or agreed to in writing, software</span></div><div class='line' id='LC12'><span class="c">#   distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span></div><div class='line' id='LC13'><span class="c">#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span></div><div class='line' id='LC14'><span class="c">#   See the License for the specific language governing permissions and</span></div><div class='line' id='LC15'><span class="c">#   limitations under the License.</span></div><div class='line' id='LC16'><span class="c">#</span></div><div class='line' id='LC17'><span class="c">#Written Python 2.7.3</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="kn">import</span> <span class="nn">urllib2</span></div><div class='line' id='LC20'><span class="kn">import</span> <span class="nn">json</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="c">### HELPERS ###</span></div><div class='line' id='LC23'><span class="n">baseURL</span> <span class="o">=</span> <span class="s">&quot;https://api.smartsheet.com/1.1&quot;</span></div><div class='line' id='LC24'><span class="n">token</span> <span class="o">=</span> <span class="s">&quot;Please Enter Your Access Token Here&quot;</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="c">###HTTP Request Abstraction###</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'><span class="k">class</span> <span class="nc">SmartsheetAPI</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Template for making calls to the Smartsheet API&quot;&quot;&quot;</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">url</span><span class="p">,</span><span class="n">token</span><span class="p">):</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">baseURL</span> <span class="o">=</span> <span class="n">url</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">token</span> <span class="o">=</span> <span class="s">&quot; Bearer &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">token</span><span class="p">)</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_raw_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">extra_header</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">method</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">request_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">baseURL</span> <span class="o">+</span> <span class="n">url</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">Request</span><span class="p">(</span><span class="n">request_url</span><span class="p">)</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span><span class="o">.</span><span class="n">add_header</span><span class="p">(</span><span class="s">&quot;Authorization&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">token</span><span class="p">)</span></div><div class='line' id='LC39'><br/></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">extra_header</span><span class="p">:</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span><span class="o">.</span><span class="n">add_header</span><span class="p">(</span><span class="n">extra_header</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">extra_header</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">data</span><span class="p">:</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span><span class="o">.</span><span class="n">add_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">method</span><span class="p">:</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">method</span> <span class="o">==</span> <span class="s">&#39;PUT&#39;</span><span class="p">:</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span><span class="o">.</span><span class="n">get_method</span> <span class="o">=</span> <span class="k">lambda</span><span class="p">:</span> <span class="s">&#39;PUT&#39;</span></div><div class='line' id='LC47'><br/></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">resp</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">req</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resp</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'><span class="n">Call</span> <span class="o">=</span> <span class="n">SmartsheetAPI</span><span class="p">(</span><span class="n">baseURL</span><span class="p">,</span><span class="n">token</span><span class="p">)</span></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'><span class="c">#Initial sheet creation</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><span class="n">columns</span> <span class="o">=</span> <span class="p">[{</span><span class="s">&quot;title&quot;</span><span class="p">:</span><span class="s">&quot;Baked Good&quot;</span><span class="p">,</span><span class="s">&quot;primary&quot;</span><span class="p">:</span><span class="bp">True</span><span class="p">,</span> <span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;TEXT_NUMBER&quot;</span><span class="p">},</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;title&quot;</span><span class="p">:</span><span class="s">&quot;Baker&quot;</span><span class="p">,</span> <span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;CONTACT_LIST&quot;</span><span class="p">},</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;title&quot;</span><span class="p">:</span><span class="s">&quot;Price Per Item&quot;</span><span class="p">,</span> <span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;TEXT_NUMBER&quot;</span><span class="p">},</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;title&quot;</span><span class="p">:</span><span class="s">&quot;Gluten Free?&quot;</span><span class="p">,</span> <span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;CHECKBOX&quot;</span><span class="p">,</span> <span class="s">&quot;symbol&quot;</span><span class="p">:</span><span class="s">&quot;FLAG&quot;</span><span class="p">},</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;title&quot;</span><span class="p">:</span><span class="s">&quot;Status&quot;</span><span class="p">,</span> <span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;PICKLIST&quot;</span><span class="p">,</span> <span class="s">&quot;options&quot;</span><span class="p">:[</span><span class="s">&quot;Started&quot;</span><span class="p">,</span><span class="s">&quot;Finished&quot;</span><span class="p">,</span><span class="s">&quot;Delivered&quot;</span><span class="p">]}]</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'><span class="n">sheet</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;name&quot;</span><span class="p">:</span><span class="s">&quot;Betty&#39;s Bake Sale&quot;</span><span class="p">,</span><span class="s">&quot;columns&quot;</span><span class="p">:</span><span class="n">columns</span><span class="p">})</span></div><div class='line' id='LC63'><br/></div><div class='line' id='LC64'><span class="n">header</span> <span class="o">=</span> <span class="s">&quot;Content-Type&quot;</span><span class="p">,</span> <span class="s">&quot; application/json&quot;</span></div><div class='line' id='LC65'><br/></div><div class='line' id='LC66'><span class="n">createSheet</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/sheets&#39;</span><span class="p">,</span> <span class="n">header</span><span class="p">,</span> <span class="n">sheet</span><span class="p">)</span> <span class="c"># Create sheet</span></div><div class='line' id='LC67'><span class="n">createSheetResp</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">Call</span><span class="o">.</span><span class="n">resp</span><span class="p">)</span></div><div class='line' id='LC68'><span class="n">sheet_id</span> <span class="o">=</span> <span class="n">createSheetResp</span><span class="p">[</span><span class="s">&#39;result&#39;</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'><span class="c">#Add a column</span></div><div class='line' id='LC71'><br/></div><div class='line' id='LC72'><span class="n">column</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;title&quot;</span><span class="p">:</span><span class="s">&quot;Delivered&quot;</span><span class="p">,</span> <span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;DATE&quot;</span><span class="p">,</span> <span class="s">&quot;index&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">})</span></div><div class='line' id='LC73'><span class="n">insert_Column</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/sheet/{}/columns&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">sheet_id</span><span class="p">),</span> <span class="n">header</span><span class="p">,</span> <span class="n">column</span><span class="p">)</span> <span class="c"># Add a column</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'><span class="c">#Add some rows</span></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'><span class="n">column_info</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/sheet/{}/columns&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">sheet_id</span><span class="p">),</span> <span class="n">header</span><span class="p">))</span></div><div class='line' id='LC79'><span class="n">row_Insert1</span> <span class="o">=</span>  <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;toTop&quot;</span><span class="p">:</span><span class="bp">True</span><span class="p">,</span> <span class="s">&quot;rows&quot;</span><span class="p">:[</span> <span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:</span> <span class="p">[</span> <span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Brownies&quot;</span><span class="p">},</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;julieanne@smartsheet.com&quot;</span><span class="p">,</span><span class="s">&quot;strict&quot;</span><span class="p">:</span> <span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;$1&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="bp">True</span><span class="p">},</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Finished&quot;</span><span class="p">},</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span> <span class="s">&quot;None&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">}]</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">},</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:[</span> <span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Snickerdoodles&quot;</span><span class="p">},</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;stevenelson@smartsheet.com&quot;</span><span class="p">,</span><span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;$1&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Delivered&quot;</span><span class="p">},</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;2013-09-04&quot;</span><span class="p">}</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]},</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:[</span> <span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Rice Krispy Treats&quot;</span><span class="p">},</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;rickthames@smartsheet.com&quot;</span><span class="p">,</span><span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;$.50&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Started&quot;</span><span class="p">},</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;None&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]},</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:[</span> <span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Muffins&quot;</span><span class="p">},</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;sandrassmart@smartsheet.com&quot;</span><span class="p">,</span><span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;$1.50&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Finished&quot;</span><span class="p">},</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;None&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]},</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:[</span> <span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Chocolate Chip Cookies&quot;</span><span class="p">},</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;janedaniels@smartsheet.com&quot;</span><span class="p">,</span><span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;$1&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Delivered&quot;</span><span class="p">},</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;2013-09-05&quot;</span><span class="p">},</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]},</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:[</span> <span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Ginger Snaps&quot;</span><span class="p">},</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;nedbarnes@smartsheet.com&quot;</span><span class="p">,</span><span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;$.50&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="bp">True</span><span class="p">},</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Unknown&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;None&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">}</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]}</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">})</span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'><span class="n">insert_Rows</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/sheet/{}/rows&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">sheet_id</span><span class="p">),</span> <span class="n">header</span><span class="p">,</span> <span class="n">row_Insert1</span><span class="p">)</span></div><div class='line' id='LC128'><span class="n">insertRowResp</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">Call</span><span class="o">.</span><span class="n">resp</span><span class="p">)</span></div><div class='line' id='LC129'><span class="n">rows</span> <span class="o">=</span> <span class="n">insertRowResp</span><span class="p">[</span><span class="s">&#39;result&#39;</span><span class="p">]</span></div><div class='line' id='LC130'><br/></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'><br/></div><div class='line' id='LC133'><br/></div><div class='line' id='LC134'><span class="c">#Move rows</span></div><div class='line' id='LC135'><span class="n">toTop</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;toTop&quot;</span><span class="p">:</span><span class="bp">True</span><span class="p">})</span></div><div class='line' id='LC136'><span class="n">move_row_up</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/row/{}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">rows</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">]),</span> <span class="n">header</span><span class="p">,</span> <span class="n">toTop</span><span class="p">,</span> <span class="s">&#39;PUT&#39;</span><span class="p">)</span></div><div class='line' id='LC137'><br/></div><div class='line' id='LC138'><span class="n">Delivered_row_info</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;toBottom&quot;</span><span class="p">:</span><span class="bp">True</span><span class="p">,</span> <span class="s">&quot;rows&quot;</span><span class="p">:[</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:</span> <span class="p">[{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">}]</span> <span class="p">},</span> <span class="c">#Blank rows to create space to help break up the sheet</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:</span> <span class="p">[{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">}]</span> <span class="p">},</span> </div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:</span> <span class="p">[{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Delivered:&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},]</span> <span class="p">}</span> <span class="p">]</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">})</span></div><div class='line' id='LC143'><br/></div><div class='line' id='LC144'><br/></div><div class='line' id='LC145'><span class="n">rowDelivered</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/sheet/{}/rows&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">sheet_id</span><span class="p">),</span> <span class="n">header</span><span class="p">,</span> <span class="n">Delivered_row_info</span><span class="p">))</span></div><div class='line' id='LC146'><br/></div><div class='line' id='LC147'><span class="n">asChild</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;parentId&quot;</span><span class="p">:</span><span class="n">rowDelivered</span><span class="p">[</span><span class="s">&#39;result&#39;</span><span class="p">][</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">]})</span></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'><br/></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'><span class="n">SnickerDoodles</span> <span class="o">=</span> <span class="n">rows</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC152'><span class="n">ChocolateChip</span> <span class="o">=</span> <span class="n">rows</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC153'><br/></div><div class='line' id='LC154'><span class="n">moveSnickerdoodles</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/row/{}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">SnickerDoodles</span><span class="p">),</span> <span class="n">header</span><span class="p">,</span> <span class="n">asChild</span><span class="p">,</span> <span class="s">&#39;PUT&#39;</span><span class="p">)</span> <span class="c">#column ID&#39;s instead of values</span></div><div class='line' id='LC155'><span class="n">Snickerdoodles_Id</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">moveSnickerdoodles</span><span class="p">)</span></div><div class='line' id='LC156'><br/></div><div class='line' id='LC157'><span class="n">asSibling</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;siblingId&quot;</span><span class="p">:</span><span class="n">Snickerdoodles_Id</span><span class="p">[</span><span class="s">&#39;result&#39;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">]})</span></div><div class='line' id='LC158'><span class="n">moveCCCookies</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/row/{}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">ChocolateChip</span><span class="p">),</span> <span class="n">header</span><span class="p">,</span> <span class="n">asSibling</span><span class="p">,</span> <span class="s">&#39;PUT&#39;</span><span class="p">)</span> <span class="c">#column ID&#39;s instead of values                    </span></div><div class='line' id='LC159'><br/></div><div class='line' id='LC160'><span class="c">#Add some more rows</span></div><div class='line' id='LC161'><span class="n">muffins</span> <span class="o">=</span> <span class="n">rows</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC162'><span class="n">row_Insert2</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;siblingId&quot;</span><span class="p">:</span><span class="n">muffins</span><span class="p">,</span> <span class="s">&quot;rows&quot;</span><span class="p">:[</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:</span> <span class="p">[{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Scones&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;tomlively@smartsheet.com&quot;</span><span class="p">,</span><span class="s">&quot;strict&quot;</span><span class="p">:</span> <span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;$1.50&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="bp">True</span><span class="p">},</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Finished&quot;</span><span class="p">},</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span> <span class="s">&quot;None&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">}</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]</span> <span class="p">},</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;cells&quot;</span><span class="p">:[</span> <span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Lemon Bars&quot;</span><span class="p">},</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;rickthames@smartsheet.com&quot;</span><span class="p">,</span><span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;$1&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">},</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;Started&quot;</span><span class="p">},</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;columnId&quot;</span><span class="p">:</span><span class="n">column_info</span><span class="p">[</span><span class="mi">5</span><span class="p">][</span><span class="s">&#39;id&#39;</span><span class="p">],</span> <span class="s">&quot;value&quot;</span><span class="p">:</span><span class="s">&quot;None&quot;</span><span class="p">,</span> <span class="s">&quot;strict&quot;</span><span class="p">:</span><span class="bp">False</span><span class="p">}</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]</span> <span class="p">}</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">})</span></div><div class='line' id='LC179'><br/></div><div class='line' id='LC180'><span class="n">insert_Rows2</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/sheet/{}/rows&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">sheet_id</span><span class="p">),</span> <span class="n">header</span><span class="p">,</span> <span class="n">row_Insert2</span><span class="p">)</span></div><div class='line' id='LC181'><br/></div><div class='line' id='LC182'><br/></div><div class='line' id='LC183'><span class="c">#Move column</span></div><div class='line' id='LC184'><span class="n">get_columns</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/sheet/{}/columns&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">sheet_id</span><span class="p">)))</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'><span class="k">for</span> <span class="n">columns</span> <span class="ow">in</span> <span class="n">get_columns</span><span class="p">:</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">columns</span><span class="p">[</span><span class="s">&#39;title&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;Status&#39;</span><span class="p">:</span> <span class="c">#Move &#39;Status&#39; to column 2</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">columnID</span> <span class="o">=</span> <span class="n">columns</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">location</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;title&quot;</span><span class="p">:</span><span class="s">&#39;Status&#39;</span><span class="p">,</span> <span class="s">&quot;index&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;sheetId&quot;</span><span class="p">:</span><span class="n">sheet_id</span><span class="p">})</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">move_column</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/column/{}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">columnID</span><span class="p">),</span> <span class="n">header</span><span class="p">,</span> <span class="n">location</span><span class="p">,</span> <span class="s">&#39;PUT&#39;</span><span class="p">)</span></div><div class='line' id='LC191'><br/></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">columns</span><span class="p">[</span><span class="s">&#39;title&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;Delivered&#39;</span><span class="p">:</span><span class="c">#Move &#39;Delivered&#39; to column 3</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">columnID</span> <span class="o">=</span> <span class="n">columns</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">location1</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;title&quot;</span><span class="p">:</span><span class="s">&#39;Delivered&#39;</span><span class="p">,</span> <span class="s">&quot;index&quot;</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span> <span class="s">&quot;sheetId&quot;</span><span class="p">:</span><span class="n">sheet_id</span><span class="p">})</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">move_column</span> <span class="o">=</span> <span class="n">Call</span><span class="o">.</span><span class="n">_raw_request</span><span class="p">(</span><span class="s">&#39;/column/{}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">columnID</span><span class="p">),</span> <span class="n">header</span><span class="p">,</span> <span class="n">location1</span><span class="p">,</span> <span class="s">&#39;PUT&#39;</span><span class="p">)</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC198'><br/></div><div class='line' id='LC199'><br/></div><div class='line' id='LC200'><br/></div><div class='line' id='LC201'><br/></div><div class='line' id='LC202'><br/></div><div class='line' id='LC203'><br/></div></pre></div>
          </td>
        </tr>
      </table>
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


    <p class="right">&copy; 2013 <span title="0.17680s from fe17.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
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

    
    <span id='server_response_time' data-time='0.17724' data-host='fe17'></span>
    
  </body>
</html>

