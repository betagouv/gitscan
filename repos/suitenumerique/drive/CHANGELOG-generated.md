## Changelog : drive (30 derniers jours, au 29 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la recherche et au filtrage de fichiers, avec de nouvelles options pour affiner les résultats par date de modification, type de fichier, contact associé et emplacement. Une aide en ligne a été ajoutée pour faciliter l'utilisation de l'application. Des corrections de bugs et des optimisations ont également été apportées, notamment concernant la gestion des conversions de fichiers et l'analyse de sécurité.

### Évolutions fonctionnelles
- Ajout d'un menu d'aide dans le panneau latéral gauche pour guider les utilisateurs.
- Amélioration du filtre de recherche avec la possibilité de filtrer par :
    - Emplacement
    - Type de fichier
    - Contact associé
    - Date de modification (avec une plage de dates personnalisable et des préréglages comme "plus d'un an")
- Possibilité de rechercher des contacts fréquemment utilisés pour faciliter le partage.
- Amélioration de l'affichage des filtres dans la modale de recherche (scrolling).
- Ajout d'un indicateur visuel pour les fichiers en cours d'analyse.
- Amélioration de la gestion des erreurs lors du téléchargement de fichiers.

### Évolutions techniques
- Mise à jour de la bibliothèque `ui-kit` vers la version 0.24.0.
- Optimisation du streaming des fichiers exportés depuis S3 pour éviter la mise en mémoire tampon.
- Amélioration de la gestion des requêtes de conversion de fichiers pendant l'analyse.
- Utilisation de JWT pour signer les requêtes de conversion OnlyOffice, améliorant la sécurité.
- Correction de la configuration du healthcheck Collabora pour fonctionner sans `curl`.
- Mise à jour des dépendances `PyJWT` et `cryptography` pour corriger des failles de sécurité.
- Refactorisation de la gestion des filtres dans l'explorateur de fichiers pour une meilleure maintenabilité.
- Extraction des requêtes de localisation des éléments pour une meilleure organisation du code.

### Autres changements
- Amélioration de la documentation README pour plus de clarté et de cohérence.
- Enrichissement des directives de contribution.
- Amélioration des fixtures de démonstration pour le partage.
- Correction de tests E2E pour assurer la couverture des nouvelles fonctionnalités.
- Mise à jour de la version de publication à 0.19.0.
- Amélioration de la formulation du contenu de la modale de conversion.
