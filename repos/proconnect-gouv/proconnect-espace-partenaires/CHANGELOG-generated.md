## Changelog : proconnect-espace-partenaires (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, l'espace partenaires a bénéficié d'améliorations significatives en termes de sécurité et de gestion des accès, notamment avec l'ajout d'une checklist de conformité MFA pour les Fournisseurs d'Identité (FI) et la possibilité pour les partenaires d'ajouter des collaborateurs. Des corrections de bugs et des améliorations de la documentation ont également été apportées. Une annonce concernant la migration vers ProConnect est maintenant visible dans l'interface.

### Évolutions fonctionnelles
- Les partenaires peuvent maintenant supprimer leurs applications. [#416](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/416)
- Ajout d'un bouton ProConnect pour faciliter l'accès. [#361](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/361) et [#413](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/413)
- Possibilité pour les partenaires d'ajouter des collaborateurs. [#393](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/393) et [#401](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/401)
- Une annonce concernant la migration vers ProConnect est maintenant visible dans l'interface. [#408](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/408)
- Ajout d'une checklist de conformité MFA pour les FI. [#425](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/425)

### Évolutions techniques
- Remplacement de `pcdbapi` par `api-partenaires`. [#418](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/418)
- Amélioration de la robustesse des tests en réduisant leur dépendance au sandbox ProConnect.
- Correction d'une dépendance conflictuelle avec `nodemailer`. [#409](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/409)
- Mise à jour de la configuration Docker Compose pour utiliser la nouvelle image `api-partenaires`. [#3565b0a](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/3565b0a)
- Amélioration de la compatibilité avec `npm prune` dans le CI. [#407](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/407)
- Correction d'un problème empêchant la suppression de son propre compte. [#403](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/403)

### Autres changements
- Amélioration de la documentation concernant le fonctionnement de ProConnect et le schéma de flux MFA. [#400](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/400) et [#390](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/390)
- Corrections de typos et améliorations de la formulation du bandeau ProConnect. [#399](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/399) et [#401](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/401)
- Application de Prettier pour formater le code. [#402](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/402)
- Correction du cache des dépendances dans le CI. [#427](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/427)
- Suppression de l'authentification par mail OTP.
