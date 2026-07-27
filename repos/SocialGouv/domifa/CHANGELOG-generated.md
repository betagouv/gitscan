## Changelog : domifa (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des corrections de bugs et des améliorations de sécurité, notamment concernant la gestion des adresses IP, des domaines d'emails autorisés et la protection contre les envois multiples de requêtes. Des améliorations ont également été apportées à l'interface utilisateur pour le formulaire de mot de passe et les alertes.

### Évolutions fonctionnelles
- Correction du formulaire de mot de passe sur l'interface utilisateur pour une meilleure expérience. [#2104ae6](https://github.com/SocialGouv/domifa/commit/2104ae6b11a461e77cf31fa28dffc12c1ecd4653)
- Correction de l'affichage des alertes d'avertissement sur l'interface utilisateur. [#5f3a485](https://github.com/SocialGouv/domifa/commit/5f3a4852036858c52a39dff16e9bc81115bc00d5)

### Évolutions techniques
- Ajout de domaines à la liste blanche pour les emails autorisés. [#f35c878](https://github.com/SocialGouv/domifa/commit/f35c8787e6b2a11da126807c81d48e9964d2a8c6)
- Correction de la sauvegarde des adresses IP. [#458bc5f](https://github.com/SocialGouv/domifa/commit/458bc5f179e4ff9b05be3c446e687b2fbf802b76)
- Correction de la gestion des IP uniques. [#c358003](https://github.com/SocialGouv/domifa/commit/c358003b6b0db4b6542368d04e9f11e4c777cbf1)
- Correction d'un problème d'envoi multiple de requêtes. [#f158e0b](https://github.com/SocialGouv/domifa/commit/f158e0bb0bf411546cd8ca999cdb7a4caf4d5045) et [#53789f8](https://github.com/SocialGouv/domifa/commit/53789f81d56e56627ea602109dedd5f6f1d6540b)
- Correction de l'anonymisation. [#46a5411](https://github.com/SocialGouv/domifa/commit/46a54116107742e6ca23c314d5ba78d607ae251b)

### Autres changements
- Mise à jour des dépendances et corrections de linting. [#5352630](https://github.com/SocialGouv/domifa/commit/53526305cbd0c1f7f6acb70cde0836185c82621a)
- Ajout d'emails pour certains domaines. [#af45969](https://github.com/SocialGouv/domifa/commit/af45969a717774f95a7087a1b97e7f40b929c9f8)
- Correction de problèmes internes liés à l'UA. [#2ca3cff](https://github.com/SocialGouv/domifa/commit/2ca3cff5007d018dc91e855885e7c635e03f97df) et [#fe8712a](https://github.com/SocialGouv/domifa/commit/fe8712acaac591ae425c8fd749770f21089d51e4)
- Ajout du type "autre" pour le type d'organisme. [#70f5721](https://github.com/SocialGouv/domifa/commit/70f5721eee8b01b50de3da23bd445a866d172095)
