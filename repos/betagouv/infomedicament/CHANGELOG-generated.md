## Changelog : infomedicament (30 derniers jours, au 7 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données disponibles, notamment avec l'ajout de nouvelles informations sur l'usage hospitalier et le remboursement des médicaments. Des améliorations ont également été apportées à l'affichage des notices et RCP pour les médicaments centralisés, ainsi qu'une refonte des migrations de données pour une meilleure organisation et synchronisation avec les sources de l'ANSM.

### Évolutions fonctionnelles
- Ajout des tags "Usage hospitalier" et "Remboursé" pour faciliter la recherche et le filtrage des médicaments. [#282](https://github.com/betagouv/infomedicament/issues/282)
- Amélioration de l'affichage : rendu des notices et RCP parsées pour les médicaments centralisés lorsque le contenu est disponible.
- Redirection automatique vers le premier élément de la liste pour les pages racine ATC. [#284](https://github.com/betagouv/infomedicament/issues/284) et [#65b2a0f](https://github.com/betagouv/infomedicament/commit/65b2a0f)
- Ajout des indications et des médicaments dans le résumé des données importées. [#5391c4b](https://github.com/betagouv/infomedicament/commit/5391c4b)

### Évolutions techniques
- Refonte complète des migrations de données BDPM : consolidation de 17 migrations en une seule migration `ansm_opendata_tables` pour une meilleure gestion et synchronisation avec les données de l'ANSM.
- Ajout de nouvelles tables de données BDPM : `bdpm_caracteristique`, `bdpm_document`, `bdpm_recipient`, `bdpm_composant`, `bdpm_specialite_atc`, `bdpm_classe_interaction`, `bdpm_substance_groupe_substance`, `bdpm_atc`, `bdpm_classe_clinique`, `bdpm_classe_groupe_substance`, `bdpm_element`, `bdpm_interaction`, `bdpm_specialite_classe_clinique`, `bdpm_dispositif`, `bdpm_presentation`, `bdpm_groupe_substance`, et `bdpm_specialite`.
- Correction de contraintes `notNull` incorrectes sur des colonnes autorisant les valeurs nulles dans les migrations.
- Clarification de l'utilisation de la clé Albert. [#738b7cb](https://github.com/betagouv/infomedicament/commit/738b7cb)
- Amélioration de la documentation. [#6f1f8a3](https://github.com/betagouv/infomedicament/commit/6f1f8a3)
- Ajout de `"use client"` dans tous les composants client pour éviter les erreurs. [#a15d2b9](https://github.com/betagouv/infomedicament/commit/a15d2b9)

### Autres changements
- Correction d'une duplication de fichier de migration. [#ec78d31](https://github.com/betagouv/infomedicament/commit/ec78d31)
- Correction de l'affichage du titre de page en cas de métadonnées manquantes. [#d36d1c8](https://github.com/betagouv/infomedicament/commit/d36d1c8) et [#72a3036](https://github.com/betagouv/infomedicament/commit/72a3036)
