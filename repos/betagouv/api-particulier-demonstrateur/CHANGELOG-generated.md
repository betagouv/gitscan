## Changelog : api-particulier-demonstrateur (30 derniers jours, au 14/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment via une meilleure gestion des messages d'information et une interface plus fluide pour les cas d'usage "Cantine" et "Transport". La stabilité technique est également renforcée par une mise à jour de l'environnement de développement et de la chaîne de tests.

### Évolutions fonctionnelles
- **Amélioration du parcours utilisateur** :
    - Ajout de messages d'information concernant la récupération automatique des justificatifs avant l'étape FranceConnect ([#99](https://github.com/betagouv/api-particulier-demonstrateur/issues/99)).
    - Optimisation de la page de connexion : déplacement du panneau d'information FranceConnect vers la connexion et masquage automatique pour les profils (personas) non concernés.
- **Corrections d'interface (UI)** :
    - Ajustements visuels dans le cas d'usage "Cantine" pour garantir la visibilité des alertes et un espacement correct des boutons.
    - Correction de l'affichage des boîtes d'aide (Transport/COG) pour respecter la largeur des colonnes.
    - Nettoyage de la typographie (suppression d'espaces superflus dans les textes d'aide).

### Évolutions techniques
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement de CI pour utiliser Node 24 avec `npm ci`.
- **Logique applicative** :
    - Correction de la méthode de résolution des cas d'usage basée sur le segment de l'URL (pathname).

### Autres changements
- **Maintenance et qualité du code** :
    - Mise à jour de Prettier (3.9) et reformatage de plusieurs layouts pour assurer la cohérence du style.
    - Stabilisation de l'environnement via le verrouillage des versions majeures des dépendances.
    - Automatisation des mises à jour de dépendances sur un cycle hebdomadaire.
