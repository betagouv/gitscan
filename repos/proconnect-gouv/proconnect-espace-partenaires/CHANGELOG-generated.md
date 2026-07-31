## Changelog : proconnect-espace-partenaires (30 derniers jours, au 29 juillet 2026)

### Résumé
Les dernières mises à jour de l'Espace Partenaires se concentrent sur l'amélioration de la sécurité avec l'introduction d'une checklist de conformité MFA pour les Fournisseurs d'Identité (FI), l'annonce de la migration vers ProConnect et la possibilité pour les partenaires d'ajouter des collaborateurs. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Les partenaires peuvent désormais supprimer leurs applications. [#416](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/416)
- Possibilité pour les partenaires d'ajouter des collaborateurs à leur espace. [#386](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/386) et [#392](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/392)
- Un bouton ProConnect a été ajouté à l'Espace Partenaires pour faciliter la migration. [#401](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/401) et [#361](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/361)
- Une checklist de conformité MFA a été ajoutée pour les Fournisseurs d'Identité (FI). [#425](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/425)
- Une annonce concernant la migration vers ProConnect est maintenant affichée dans l'Espace Partenaires. [#408](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/408)
- Prévention de la suppression de son propre compte par les utilisateurs. [#403](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/403)

### Évolutions techniques
- Migration vers la nouvelle image `api-partenaires` dans le fichier `docker-compose`. [#418](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/418)
- Amélioration de la robustesse des tests en réduisant leur dépendance au sandbox ProConnect.
- Correction d'une dépendance conflictuelle avec `nodemailer`. [#409](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/409)
- Suppression de l'authentification par email OTP. [#388](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/388)

### Autres changements
- Améliorations de la documentation concernant le fonctionnement de ProConnect et le schéma de flux MFA. [#400](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/400) et [#390](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/390)
- Améliorations de l'interface utilisateur (front-end). [#413](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/413)
- Corrections de typos et améliorations de la formulation. [#399](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/399) et [#401](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/401)
- Application de Prettier pour formater le code. [#402](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/402)
- Ajout du dossier de configuration IntelliJ IDEA au `.gitignore`. [#391](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/391)
