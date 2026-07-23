## Changelog : infomedicament (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'affichage des informations des médicaments, notamment pour les médicaments centralisés avec l'ajout de l'affichage des notices et RCP. Une importante mise à jour des données de l'ANSM a été intégrée via de nouvelles migrations, enrichissant ainsi la base de données. Des améliorations de l'expérience utilisateur ont également été apportées, comme la redirection de la page racine ATC vers le premier élément de la liste.

### Évolutions fonctionnelles
- Ajout de tags "Usage hospitalier" et "Remboursé" pour faciliter la recherche et le filtrage des médicaments. [#282](https://github.com/betagouv/infomedicament/issues/282)
- Redirection de la page racine pour un code ATC vers le premier élément de la liste, améliorant la navigation. [#282](https://github.com/betagouv/infomedicament/issues/282) et [#65b2a0f](https://github.com/betagouv/infomedicament/commit/65b2a0f)
- Affichage des notices et RCP (Résumés des Caractéristiques du Produit) pour les médicaments centralisés lorsque le contenu est disponible.
- Amélioration de l'affichage du titre de la page en cas de métadonnées manquantes.
- Ajout des indications et des médicaments dans le résumé des données importées. [#5391c4b](https://github.com/betagouv/infomedicament/commit/5391c4b)

### Évolutions techniques
- Mise à jour des données de l'ANSM via de nouvelles migrations, incluant l'ajout de nombreuses tables (bdpm_caracteristique, bdpm_document, bdpm_recipient, etc.).
- Refactorisation des migrations BDPM pour les consolider en une seule migration `ansm_opendata_tables`.
- Correction d'une duplication de fichier de migration. [#284](https://github.com/betagouv/infomedicament/issues/284)
- Ajout de `"use client"` dans tous les composants client pour éviter les erreurs.
- Clarification de l'utilisation de la clé Albert et amélioration de la documentation.

### Autres changements
- Documentation du processus actuel de mise à jour des données.
- Amélioration de la documentation générale.
