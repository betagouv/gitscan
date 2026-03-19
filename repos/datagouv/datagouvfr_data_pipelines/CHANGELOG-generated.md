## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, les travaux sur les pipelines de données se sont concentrés sur l'amélioration de la robustesse des DAGs existants, notamment ceux liés aux élections, au Finess et au SIREN. De nouvelles fonctionnalités ont été ajoutées pour la gestion des données de pétitions du Sénat et pour la migration vers OVH S3, avec une attention particulière portée à la gestion des erreurs et à la suppression des données obsolètes.

### Évolutions fonctionnelles
- Ajout d'un nouveau DAG pour les pétitions du Sénat. [#642](https://github.com/datagouv/datagouvfr_data_pipelines/issues/642)
- Amélioration de la gestion des erreurs dans le DAG Simplifions, avec des tentatives de relance en cas d'échec. [#637](https://github.com/datagouv/datagouvfr_data_pipelines/issues/637)
- Mise en place d'un mécanisme de suppression des anciens fichiers sur le SFTP pour éviter l'accumulation de données. [#643](https://github.com/datagouv/datagouvfr_data_pipelines/issues/643)
- Simplifions : suppression des tags de budget et adaptation des mots-clés en tant que tags de sujet. [#630](https://github.com/datagouv/datagouvfr_data_pipelines/issues/630), [#638](https://github.com/datagouv/datagouvfr_data_pipelines/issues/638)

### Évolutions techniques
- Refactorisation des interactions avec S3 pour une meilleure gestion et performance. [#636](https://github.com/datagouv/datagouvfr_data_pipelines/issues/636)
- Amélioration de la gestion des types de contenu (content type) lors de l'écriture des objets sur S3. [#635](https://github.com/datagouv/datagouvfr_data_pipelines/issues/635)
- Correction de l'utilisation de l'utilisateur Debian pour le geocodage, améliorant la sécurité et la cohérence. [#644](https://github.com/datagouv/datagouvfr_data_pipelines/issues/644)
- Adaptation du DAG Finess pour gérer des données sources de mauvaise qualité. [#640](https://github.com/datagouv/datagouvfr_data_pipelines/issues/640)
- Refactorisation de la méthode de détection de court-circuit dans les DAGs SIREN. [#633](https://github.com/datagouv/datagouvfr_data_pipelines/issues/633)
- Mise en place d'un client-side copy object pour la migration vers OVH S3. [#631](https://github.com/datagouv/datagouvfr_data_pipelines/issues/631)
- Correction de la gestion du NIC (numéro d'identification du corps) dans le DAG de publication SIREN, en s'assurant qu'il est traité comme une chaîne de caractères. [#632](https://github.com/datagouv/datagouvfr_data_pipelines/issues/632)

### Autres changements
- Ajout de vérifications de cohérence (sanity checks) dans le DAG des élections.
- Amélioration des logs pour faciliter le débogage.
- Nettoyage du code et des noms de fichiers/dossiers.
- Corrections de typos et de références obsolètes.
- Application de linters pour améliorer la qualité du code.
