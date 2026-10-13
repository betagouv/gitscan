## Changelog : pitchou (30 derniers jours, au 12 octobre 2026)

### Résumé
Ce mois-ci, Pitchou a bénéficié d'une refonte visuelle majeure et d'améliorations ergonomiques significatives, notamment pour faciliter la saisie sur différents types d'écrans. L'outil gagne en efficacité avec de nouvelles options d'exportation de données (CSV, ODS) et une gestion des fichiers plus rapide grâce à un nouveau mode d'envoi direct.

### Évolutions fonctionnelles
- Exportation des dossiers filtrés aux formats CSV et ODS [#710](https://github.com/betagouv/pitchou/issues/710).
- Ajout de la gestion des décisions requises, de l'UICN et de la possibilité de supprimer des pièces jointes [#705](https://github.com/betagouv/pitchou/issues/705).
- Refonte complète de l'interface utilisateur pour une expérience plus moderne [#685](https://github.com/betagouv/pitchou/issues/685).
- Améliorations de l'ergonomie : mise en page responsive pour la saisie des espèces [#706](https://github.com/betagouv/pitchou/issues/706) et optimisation de la navigation dans les dossiers (onglets, pagination, boutons d'action) [#707](https://github.com/betagouv/pitchou/issues/707).
- Extension de l'authentification pour autoriser les adresses e-mail du domaine `indre.gouv.fr`.
- Corrections de bugs : correction d'une coquille sur les labels de perturbation [#713](https://github.com/betagouv/pitchou/issues/713) et suppression d'une notification de doublons sur les champs obligatoires [#711](https://github.com/betagouv/pitchou/issues/711).

### Évolutions techniques
- Optimisation du stockage avec la mise en place de l'upload direct des fichiers vers S3 [#704](https://github.com/betagouv/pitchou/issues/704).
- Évolution de la base de données pour intégrer la structure des porteurs de projet [#709](https://github.com/betagouv/pitchou/issues/709).

### Autres changements
- Nettoyage de l'interface d'administration suite au retrait de la fonctionnalité de téléchargement de dossiers.
