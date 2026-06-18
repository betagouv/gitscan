## Changelog : api-subventions-asso (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, l'API a bénéficié d'améliorations significatives concernant la gestion des subventions Osiris, avec l'ajout de nouvelles routes et d'une meilleure intégration des données. Des corrections ont également été apportées pour améliorer la robustesse et la précision des données traitées, notamment en gérant différents formats numériques et en normalisant les données RNA.

### Évolutions fonctionnelles
- Ajout de nouvelles routes pour accéder aux détails des subventions Osiris, permettant une intégration plus fine avec cette source de données. [#3840](https://github.com/betagouv/api-subventions-asso/issues/3840)
- Amélioration de la détection des nouveaux fichiers Chorus sur le bucket S3, assurant une mise à jour plus rapide des informations sur les subventions. [#3931](https://github.com/betagouv/api-subventions-asso/issues/3931)
- Ajout d'un tag après l'import des données, facilitant leur identification et leur suivi. [#3932](https://github.com/betagouv/api-subventions-asso/issues/3932)
- Normalisation des RNA (numéros de référence des associations) pour permettre une recherche insensible à la casse. [#3862](https://github.com/betagouv/api-subventions-asso/issues/3862)
- Gestion des formats numériques européens utilisant la virgule comme séparateur décimal. [#3955](https://github.com/betagouv/api-subventions-asso/issues/3955)
- Correction de l'envoi de paramètres vides à l'API Brevo Transaction. [#3822](https://github.com/betagouv/api-subventions-asso/issues/3822)

### Évolutions techniques
- Refactorisation du code pour renommer les variables `uniteLegalEntrepriseXXX` en `uniteLegaleEntrepriseXXX` pour une meilleure cohérence. [#3888](https://github.com/betagouv/api-subventions-asso/issues/3888)
- Migration du service `api-asso` vers une architecture basée sur des adaptateurs et des ports, améliorant la modularité et la testabilité. [#3549](https://github.com/betagouv/api-subventions-asso/issues/3549)
- Validation des requêtes pour une meilleure robustesse de l'API. [#3906](https://github.com/betagouv/api-subventions-asso/issues/3906)
- Mise à jour de la configuration TypeScript avec l'ajout de `todos` pour faciliter la maintenance du code. [#3904](https://github.com/betagouv/api-subventions-asso/issues/3904)
- Ajout de documentation expliquant la différence entre les endpoints de téléchargement par association et par document. [#3927](https://github.com/betagouv/api-subventions-asso/issues/3927)

### Autres changements
- Ajout de la dernière agrégation à la documentation de l'API. [#3928](https://github.com/betagouv/api-subventions-asso/issues/3928)
- Mise à jour des dépendances du frontend. [#3922](https://github.com/betagouv/api-subventions-asso/issues/3922)
- Correction du fichier `Procfile`. [#0000](https://github.com/betagouv/api-subventions-asso/issues/0000)
- Ajout du fichier `.versionrc.json`. [#0000](https://github.com/betagouv/api-subventions-asso/issues/0000)
- Correction du fichier `CHANGELOG.md`. [#0000](https://github.com/betagouv/api-subventions-asso/issues/0000)
