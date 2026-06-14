## Changelog : Docurba (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Docurba se concentrent sur l'amélioration de l'interface utilisateur Nuxt3, notamment dans la gestion des événements et des procédures, ainsi que sur des optimisations de l'API Django et de l'infrastructure. Des corrections de bugs et des améliorations de la performance ont également été apportées. L'authentification Supabase est en cours d'implémentation.

### Évolutions fonctionnelles
- L'interface Nuxt3 a été améliorée pour afficher et filtrer les événements plus efficacement, notamment en indiquant si une procédure est antérieure ou postérieure à la loi Huwart. [#29296c3](https://github.com/MTES-MCT/Docurba/commit/29296c3)
- Les procédures des collectivités sont maintenant récupérées via l'API Django dans l'interface Nuxt3. [#9f70b80](https://github.com/MTES-MCT/Docurba/commit/9f70b80)
- La page de lecture des PAC (Prescriptions Architecturales et Constructives) est désormais publique. [#b53a072](https://github.com/MTES-MCT/Docurba/commit/b53a072)
- Amélioration de l'affichage des événements dans la liste, avec des informations plus claires sur leur statut. [#81b258b](https://github.com/MTES-MCT/Docurba/commit/81b258b)
- Possibilité de filtrer les types de procédures en fonction de leur date de début. [#4f89e20](https://github.com/MTES-MCT/Docurba/commit/4f89e20)
- Ajout d'un label pour les procédures antérieures à la loi Huwart. [#17db8cc](https://github.com/MTES-MCT/Docurba/commit/17db8cc)
- L'interface d'édition des événements a été améliorée pour détecter et signaler les erreurs. [#3d9205b](https://github.com/MTES-MCT/Docurba/commit/3d9205b)
- Amélioration de la gestion des événements de prescription, avec détection de tous les événements et filtrage des événements invalides. [#13efcf1](https://github.com/MTES-MCT/Docurba/commit/13efcf1) et [#35722bb](https://github.com/MTES-MCT/Docurba/commit/35722bb)
- Ajout de nouvelles catégories de PAC et d'une catégorie d'événement dans l'API Django. [#a553a34](https://github.com/MTES-MCT/Docurba/commit/a553a34), [#a26bfc2](https://github.com/MTES-MCT/Docurba/commit/a26bfc2) et [#775c627](https://github.com/MTES-MCT/Docurba/commit/775c627)

### Évolutions techniques
- Implémentation de l'authentification Supabase avec ajout des dépendances nécessaires et configuration. [#9b990ef](https://github.com/MTES-MCT/Docurba/commit/9b990ef), [#a386c1e](https://github.com/MTES-MCT/Docurba/commit/a386c1e), [#6b7b258](https://github.com/MTES-MCT/Docurba/commit/6b7b258), [#45a42e5](https://github.com/MTES-MCT/Docurba/commit/45a42e5), [#03c9e9a](https://github.com/MTES-MCT/Docurba/commit/03c9e9a) et [#5fb90e3](https://github.com/MTES-MCT/Docurba/commit/5fb90e3)
- Refonte de l'infrastructure avec remplacement de `wget` par `curl`, ajout de Nginx pour servir les fichiers statiques et mise en place de la limitation de débit. [#f040adc](https://github.com/MTES-MCT/Docurba/commit/f040adc), [#dcb5c6e](https://github.com/MTES-MCT/Docurba/commit/dcb5c6e), [#9e8e1a9](https://github.com/MTES-MCT/Docurba/commit/9e8e1a9) et [#74ec84d](https://github.com/MTES-MCT/Docurba/commit/74ec84d)
- Ajout d'alertes Slack lors des déploiements. [#6209a5c](https://github.com/MTES-MCT/Docurba/commit/6209a5c)
- Amélioration des performances de l'API Django avec l'ajout de tests, la sélection des champs à afficher dans l'admin et l'ajout d'index. [#fff3ebf](https://github.com/MTES-MCT/Docurba/commit/fff3ebf), [#60194b2](https://github.com/MTES-MCT/Docurba/commit/60194b2) et [#207d50b](https://github.com/MTES-MCT/Docurba/commit/207d50b)
- Utilisation de l'URL de l'API Docurba à partir d'une variable d'environnement dans Nuxt3. [#bcaf256](https://github.com/MTES-MCT/Docurba/commit/bcaf256)
- Ajout d'un champ `last_sign_in_at` au modèle User et d'un modèle Session. [#fff6e6f](https://github.com/MTES-MCT/Docurba/commit/fff6e6f) et [#e4364f2](https://github.com/MTES-MCT/Docurba/commit/e4364f2)

### Autres changements
- Mise à jour des dépendances : `ruff`, `supabase`, `django`, `django-filter`, `cryptography`.
- Configuration de Dependabot pour vérifier les mises à jour disponibles quotidiennement. [#12842da](https://github.com/MTES-MCT/Docurba/commit/12842da)
- Amélioration de la documentation et des commentaires dans le code.
- Corrections mineures et refactorisation du code.
- Ajout d'un header Supabase-Authorization. [#aed41e](https://github.com/MTES-MCT/Docurba/commit/aed41e)
