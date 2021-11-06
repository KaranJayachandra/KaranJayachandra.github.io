# Source for the gems
source "https://rubygems.org"

# Allow for HTTPS connections
gem "webrick"

# The used gems for additional customization
group :jekyll_plugins do
  # Gem to allow for hosting on GitHub Pages
  gem "github-pages", "~> 219"
  # Can generate an atom feed for posts
  gem "jekyll-feed", "~> 0.12"
  # Gem to allow for added support or table
  gem "jekyll-spaceship"
end

# Gems to allow for time zone data manipulation
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]