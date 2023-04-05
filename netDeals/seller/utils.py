
def is_approved_seller(user):
    if user.is_authenticated and hasattr(user, 'sellerprofile'):
        return user.sellerprofile.is_approved
    return False

# def is_seller_approved(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         seller = SellerProfile.objects.get(user=request.user)
#         if seller.approved:
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('seller:restricted_access')  # Update the URL namespace
#     return _wrapped_view
# def is_seller_approved(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         return user_passes_test(
#             is_approved_seller, login_url='/restricted_access/'
#         )(view_func)(request, *args, **kwargs)
#     return _wrapped_view