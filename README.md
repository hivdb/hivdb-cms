# HIVDB CMS

Content Management System of HIVDB Website


## Folder Structure

- `pages/`: where we stores YAML files. A file starts with "page-" is
  automatically corresponded to a page on HIVDB website starts with "/page/".
  For example, "page-example.yml" is corresponded to page "/page/example/".
- `resources/`: for any YAML files in `pages/`, the user can specify a magic
  keyword `_resources` to refer to a file in this folder. The CMS system
  currently support both Markdown (`.md`) and HTML (`.html`) files. However
  please always choose Markdown as your first option since it's simpler and
  formatted more well than HTML file.
- `images/`: image files. You can use `$$CMS_PREFIX$$images/example.png` to
  refer to a image from this folder.
- `downloads/`: other files needed to be made downloadable. You can use
  `$$CMS_PREFIX$$downloads/example.txt` to refer to a file from this folder.

## Usage

### Prerequisites

- Docker: Follow https://docs.docker.com/install/ to install Docker on your
  computer.
- AWS IAM credential: Follow https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html
  to configure the credential. Your IAM must have the access to AWS S3.

If you have sudo access to the internal server `zhangfei`, it is already
configured under username "philip":

```bash
ssh zhangfei
sudo su - philip
cd ~/gitrepo/hivdb-cms
```

### Deployment

Several deployment commands are available for different targets:

```bash
# always pull the latest version first
git pull

# build and deploy to localhost test environment:
make deploy-localhost

# build and deploy to staging.hivdb.org:
make deploy-staging

# build and deploy to staging2.hivdb.org:
make deploy-staging2

# build and deploy to hivdb.stanford.edu:
make deploy-prod

# build and deploy to all targets:
make deploy-all
```

After a deployment was made to hivdb.stanford.edu, you need to invalidate all cached files here:

https://console.aws.amazon.com/cloudfront/home?region=us-west-2#distribution-settings:ED0OYJBLR1U2Y


### Rebuild Docker image

We have prebuilt Docker "hivdb-cms-builder" images available on
[Docker Hub][docker-hub-link]. The image includes all dependencies needed by
`build.py`. Usually we don't need to rebuild the "builder" image. However,
in case we need to rebuild the image:

```bash
# Please ask Philip for credential of DockerHub account
make build-docker push-docker
```

[docker-hub-link]: https://hub.docker.com/r/hivdb/hivdb-cms-builder
