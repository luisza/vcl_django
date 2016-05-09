from django.contrib import admin

# Register your models here.
from image.models import (Ostype,
                            Imagetype,
                            Os,
                            Imagemeta,
                            Image,
                            Subimages,
                            Imagerevision,
                            Imagerevisioninfo,
                        
                            Winkms,
                            Winproductkey,
                            Connectmethod,
                            Connectmethodmap,
                            Connectmethodport)

admin.site.register([Ostype,
                    Imagetype,
                    Os,
                    Imagemeta,
                    Image,
                    Subimages,
                    Imagerevision,
                    Imagerevisioninfo,
                   
                    Winkms,
                    Winproductkey,
                    Connectmethod,
                    Connectmethodmap,
                    Connectmethodport])