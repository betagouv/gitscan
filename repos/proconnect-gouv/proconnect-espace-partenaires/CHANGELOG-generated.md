## Changelog : proconnect-espace-partenaires (30 derniers jours, au 05 août 2026)

### Résumé
Les récentes évolutions se concentrent sur la préparation de la migration vers ProConnect et l'amélioration de l'autonomie des partenaires. De nouvelles fonctionnalités de gestion ont été introduites, comme la possibilité de supprimer une application, tandis que l'interface utilisateur a été affinée pour une meilleure clarté. Côté technique, l'infrastructure a été modernisée pour assurer une transition fluide vers les nouveaux services API.

### Évolutions fonctionnelles
- **Gestion des applications** : Ajout de la possibilité pour les partenaires de supprimer leur propre application [#416](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/416).
- **Expérience utilisateur et interface** :
    - Amélioration visuelle globale de l'interface [#413](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/413).
    - Ajout d'un bouton d'accès direct à ProConnect [#361](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/361).
    - Mise en place d'une checklist pour les partenaires FI [#425](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/425).
- **Communication et migration** : Clarification des messages d'annonce et du bandeau d'information concernant la migration vers ProConnect [#408](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/408), [#417](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/417).
- **Sécurité et accès** : Masquage de l'option de connexion par "Magic Link" et documentation sur les procédures de récupération de compte [#430](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/430).

### Évolutions techniques
- **Architecture et Infrastructure** :
    - Migration de l'API vers la nouvelle image `api-partenaires` (remplacement de `pcdbapi`) [#418](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/418).
    - Mise à jour de la configuration Docker Compose pour supporter la nouvelle image API.
- **CI/CD et Tests** :
    - Optimisation des pipelines de CI en améliorant la gestion du cache `node_modules` [#427](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/427).
    - Amélioration de la fiabilité des tests en réduisant leur dépendance vis-à-vis du sandbox ProConnect.
    - Validation de la compatibilité de la commande `npm prune` dans le cycle de CI [#407](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/407).
- **Maintenance** : Résolution d'un conflit de dépendances sur le package Nodemailer [#409](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/409).

### Autres changements
- **Documentation** : Mise à jour du lien du Portail Partenaire pour utiliser le protocole HTTPS [#432](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/432).
