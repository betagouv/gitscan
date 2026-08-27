## Changelog : seves (30 derniers jours, au 26 août 2026)

### Résumé
Les évolutions de ce mois se concentrent sur l'enrichissement du module des Situations d'Alerte (SA) et des événements liés au domaine animal. L'expérience utilisateur a été considérablement améliorée par l'automatisation de la saisie de données (via les services SIRENE et BAN), une meilleure gestion de la cartographie et l'ajout de nouveaux composants d'interface pour sécuriser les actions critiques (modales de confirmation, alertes d'extraction).

### Évolutions fonctionnelles
- **Gestion des Situations d'Alerte (SA) :**
    - Création d'une vue détaillée incluant l'historique et des filtres de recherche [#2220].
    - Ajout de nouveaux blocs d'information pour enrichir les dossiers (contexte, liste des maladies, bloc détenteur) [#2205].
    - Intégration d'une nouvelle icône pour identifier plus facilement les SA dans les listes [#2214].
- **Événements Animaux :** Ajout de blocs de mesures, de localisation et mise à jour de la numérotation spécifique.
- **Cartographie & SIG :**
    - Affichage des parcelles agricoles sur la carte [#2221].
    - Possibilité de définir le style de carte initial (ex: vue satellite) directement dans les formulaires [#2213].
- **Saisie et Expérience Utilisateur :**
    - Pré-remplissage automatique des données des détenteurs (particuliers et entreprises) via les API SIRENE et BAN.
    - Amélioration du composant de sélection hiérarchique (*treeselect*) avec gestion des messages "aucun résultat" et des mécanismes de champs obligatoires.
    - Ajout d'infobulles sur le statut des animaux [#2211].
    - Mise en place de modales de confirmation pour sécuriser le changement de type d'établissement [#2215] et d'alertes pour les extractions de données volumineuses [#2179].
    - Optimisation des notifications : suppression des alertes de contact lors de la simple mise à jour d'événements pour réduire le bruit inutile [#2194, #2196].

### Évolutions techniques
- **Architecture & Données :**
    - Implémentation du domaine SA, incluant la configuration du système et la mise à jour des middlewares [#2216].
    - Création de nouvelles vues matérialisées pour optimiser les performances des tableaux de bord Metabase.
- **Sécurité :**
    - Renforcement de la sécurité avec l'ajout du header `X-XSS-Protection`.
    - Sécurisation du traitement des documents : suppression automatique du JavaScript des fichiers PDF avant leur analyse.
    - Amélioration de la validation des fichiers lors de l'upload.
- **Maintenance & Infrastructure :**
    - Correction d'un problème de déploiement lié à la bibliothèque GDAL.
    - Résolution de bugs d'interface sur le focus du composant *treeselect*.
