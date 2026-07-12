## Changelog : infomedicament (30 derniers jours, au 7 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données disponibles, notamment avec l'ajout de nouvelles informations sur les médicaments pédiatriques et les données BDPM, ainsi que sur l'amélioration de la recherche et de la navigation sur le site. Des optimisations de performance ont également été apportées pour accélérer le chargement des pages.

### Évolutions fonctionnelles
- Ajout de tags "Usage hospitalier" et "Remboursé" pour faciliter le filtrage des médicaments. [#282](https://github.com/betagouv/infomedicament/issues/282)
- Redirection automatique de la page racine des listes de médicaments vers la première lettre de la liste pour une navigation plus intuitive.
- Affichage des notices et RCP (Résumé des Caractéristiques du Produit) pour les médicaments centralisés lorsque le contenu est disponible.
- Amélioration de la recherche avec l'ajout de synonymes pour les termes courants, et suggestion de corrections orthographiques ("Vouliez-vous dire").
- Classement et autocomplétion des résultats de recherche au niveau de la spécialité.
- Ajout de pages dédiées aux médicaments pédiatriques.
- Mise à jour des informations globales de notation.
- Ajout de nouvelles pages au sitemap pour une meilleure indexation par les moteurs de recherche.

### Évolutions techniques
- Refactorisation et consolidation des migrations de la base de données BDPM pour une meilleure organisation et performance.
- Ajout de nouvelles tables à la base de données pour stocker les données BDPM (bdpm_caracteristique, bdpm_document, bdpm_recipient, bdpm_composant, bdpm_specialite_atc, etc.).
- Optimisation de la population de la table `spec_metadata` pour éviter les erreurs de mémoire insuffisante (OOM) sur Scalingo.
- Pré-rendu des 500 médicaments les plus consultés lors de la construction du site pour améliorer la vitesse de chargement.
- Utilisation de "use client" dans tous les composants client pour éviter les erreurs Next.js.
- Correction de plusieurs erreurs et réversions de modifications récentes pour assurer la stabilité du site.

### Autres changements
- Clarification de l'utilisation de la clé Albert.
- Amélioration de la documentation.
- Correction de la duplication d'un fichier de migration. [#284](https://github.com/betagouv/infomedicament/issues/284)
- Ajout d'informations sur les indications et les médicaments dans le résumé des données importées.
- Correction de bugs mineurs liés à la structure des pages et à l'affichage des données.
