## Changelog : seves (30 derniers jours, au 11 novembre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de l'ergonomie des formulaires de saisie et de la gestion des événements. Les utilisateurs bénéficient désormais de fonctionnalités de traitement par lot, d'une meilleure validation des données pour garantir la cohérence des dossiers, et d'une interface plus intuitive pour le suivi des événements sanitaires.

### Évolutions fonctionnelles
- **Gestion des événements et des données :**
    - Possibilité de clôturer le suivi de plusieurs événements simultanément.
    - Autorisation de la modification des événements animaux.
    - Amélioration de la gestion des analyses : prise en compte des cas où la maladie détectée diffère de celle de l'événement initial.
    - Sécurisation des données : impossibilité de supprimer des éléments (repas, aliments) déjà utilisés dans une conclusion.
- **Optimisation de la saisie et des formulaires :**
    - Renforcement des contrôles de cohérence (ordre chronologique des dates, dates de résultats obligatoires si confirmées, contraintes de format pour les cas de TIAC).
    - Automatisation et aide à la saisie (pré-sélection des dangers selon la source, gestion automatique du pays lors du choix d'une commune, masquage contextuel de champs pour les animaux sauvages).
    - Amélioration des sélecteurs (recherche dans les listes de laboratoires, regroupement des espèces les plus fréquentes, fermeture automatique des menus déroulants).
- **Interface utilisateur (UI/UX) :**
    - Refonte visuelle de la page de détails des événements animaux et amélioration de la mise en page des tableaux.
    - Clarification des actions critiques (boutons de suppression mis en évidence en rouge avec icône de corbeille).
    - Amélioration de la lisibilité (mise en évidence des messages non lus, noms raccourcis dans les listes).
    - Amélioration de la cartographie (centrage automatique lors de la sélection d'une ville).
- **Communication et notifications :**
    - Possibilité de configurer des notices HTML personnalisées par domaine.
    - Amélioration des bannières d'alerte incluant le nom de la maladie détectée.
    - Correction du formatage lors du copier-coller de texte dans les messages.

### Évolutions techniques
- **Performance et CI/CD :**
    - Accélération des suites de tests (optimisation des méthodes de nettoyage de base de données).
    - Optimisation des workflows GitHub Actions via la mise en cache des paquets.
- **Sécurité et Infrastructure :**
    - Optimisation des règles du WAF pour réduire les faux positifs et exclure certains jetons de sécurité (OIDC, PostHog).
    - Renforcement de la sécurité lors de la création de fiches de zone.
    - Nettoyage du code par la suppression des vues matérialisées.
- **Base de données :**
    - Ajout de contraintes d'intégrité pour les mesures de gestion.
    - Résolution de conflits lors de la fusion des migrations.

### Autres changements
- Ajout d'un fichier `Security.md` pour documenter les politiques de sécurité.
