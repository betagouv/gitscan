## Changelog : mon-entreprise (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois a été marqué par des évolutions majeures, notamment le lancement d'un outil permettant de comparer différents modèles d'entreprise et une refonte complète de la page d'accueil. Les simulateurs ont été affinés pour plus de précision, particulièrement pour les utilisateurs de Mayotte, et la documentation a été largement modernisée pour offrir une meilleure expérience de consultation des règles métier.

### Évolutions fonctionnelles
- **Nouveau comparateur de modèles** : possibilité de comparer plusieurs statuts (ex: SASU, EI) en fonction d'objectifs précis (IR/IS, versement libératoire) et avec des périodes de calcul flexibles (mensuelles ou annuelles).
- **Nouveaux simulateurs** : intégration des simulateurs dédiés aux profils Artisan et Commerçant.
- **Mise à jour du simulateur Lodeom** : 
    - Intégration complète des spécificités réglementaires et des taux pour Mayotte.
    - Simplification du parcours utilisateur en supprimant des questions redondantes ou non applicables.
    - Corrections sur le calcul des heures supplémentaires et de la rémunération brute.
- **Refonte de la page d'accueil** : nouvelle interface plus intuitive incluant des sections "Qui sommes-nous", "Explorer les statuts" et un moteur de recherche/création direct.
- **Améliorations des simulateurs existants** : corrections sur les calculs de la SASU (unités d'exonération) et de l'Impôt sur le Revenu (dividendes).

### Évolutions techniques
- **Refonte logicielle** : restructuration profonde du module de comparaison et de la logique de gestion des montants pour améliorer la maintenabilité du code.
- **Automatisation de la qualité (CI/CD)** : mise en place d'une revue de code automatisée par intelligence artificielle (Claude) pour accélérer les cycles de développement.
- **Optimisation du déploiement** : amélioration de la gestion des "Review Apps" pour des tests plus fiables et rapides.
- **Accessibilité (a11y)** : corrections importantes des labels ARIA, de la gestion des contrastes de couleurs et de la navigation au clavier, notamment dans les formulaires.
- **Performance et Tracking** : optimisation du chargement du tracking (Piano Analytics) et correction de problèmes liés au rendu côté serveur (SSR).

### Autres changements
- **Modernisation de la documentation** : passage au format MDX pour une meilleure gestion du contenu, amélioration de la visualisation des règles Publicodes et mise à jour de la documentation de l'API.
- **Internationalisation (i18n)** : corrections de nombreuses traductions et uniformisation de la langue sur l'ensemble des composants.
- **Nettoyage** : suppression de composants et de règles obsolètes pour alléger l'application.
