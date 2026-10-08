## Changelog : nitrates (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois a été marqué par une mise à jour majeure de l'interface cartographique et une mise en conformité importante des pages légales. Le projet a également intégré les nouvelles données réglementaires pour la Bretagne (PAR Bretagne 2026) et a renforcé ses outils d'administration pour permettre une gestion plus souple des calendriers d'épandage.

### Évolutions fonctionnelles
- **Cartographie et simulateur** : 
    - Amélioration significative de l'ergonomie de la carte : gestion du plein écran, raccourcis clavier, états de chargement des zones et mémorisation des couches actives [#531].
    - Mise à jour des couleurs des zones (ZV) avec une nouvelle palette et des niveaux de remplissage ajustés, désormais modifiables via l'administration [#555].
    - Correction d'un bug empêchant la soumission du formulaire lors de la consultation du dépliant réglementaire.
- **Données et réglementation** :
    - Intégration des données et du zonage pour le PAR Bretagne 2026 [#566].
    - Enrichissement des blocs de "Questions Complémentaires" (PC) avec des liens syndiqués et des contenus plus détaillés [#467, #254].
- **Interface et accessibilité** :
    - Mise en conformité des pages légales (CGU, accessibilité, données personnelles) suite aux retours juridiques [#550].
    - Amélioration de l'accessibilité via l'adoption des composants DSFR (champs de dates, badges de rappel) [#252, #487].
    - Ajout d'un encart d'aide contextuel (exit-intent) pour guider l'utilisateur [#435].

### Évolutions techniques
- **Administration** : Création d'une nouvelle "matrice" de gestion des calendriers d'épandage (playground) permettant de configurer plus facilement les questions complémentaires et les périodes de couverture [#529].
- **Observabilité et performance** : 
    - Intégration de la télémétrie infrastructure via Sentry pour un meilleur suivi des erreurs [#476].
    - Optimisation des performances de Gunicorn sur l'environnement de staging [#456].
- **Gestion des données SIG** : Mise en place d'un versionnement des couches SIG et d'une gestion par millésime pour garantir la cohérence des données affichées [#492].
- **SEO et Web** : Optimisation du référencement et de l'accessibilité pour les modèles d'IA via l'implémentation de `robots.txt`, `sitemap.xml` et `llms.txt` [#565, #290].
- **Sécurité** : Mise à jour de la politique de sécurité du contenu (CSP) pour autoriser les médias de domaines spécifiques [#547].

### Autres changements
- **Hygiène du dépôt** : Nettoyage de la documentation (README), suppression d'outils obsolètes et restructuration des tests pour une meilleure couverture du code.
