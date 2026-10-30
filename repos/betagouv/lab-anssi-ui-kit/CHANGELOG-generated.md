## Changelog : lab-anssi-ui-kit (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci a été marqué par une étape majeure avec le passage à la version 2.0.0. Les évolutions se concentrent sur une plus grande flexibilité des composants (via l'ajout de "slots" permettant d'insérer du contenu personnalisé), une intégration Svelte nettement plus robuste et un renforcement massif de la fiabilité grâce à une couverture de tests étendue sur l'ensemble de la bibliothèque.

### Évolutions fonctionnelles
- **Nouveaux composants et fonctionnalités :**
    - Ajout du composant `Combobox` au sein du DSFR.
    - Améliorations du `DsfrCombobox` : ajout du filtrage par légende de groupe, gestion optimisée du bouton "Tout sélectionner", ajout d'une largeur minimale personnalisable et correction des animations.
    - Évolutions du `FiltresCatalogue` : ajout d'une variation "liens" et amélioration des styles.
- **Flexibilité accrue des composants :**
    - Introduction massive de "slots" (emplacements de contenu personnalisables) et de propriétés optionnelles sur de nombreux composants DSFR et Lab (ex: `DsfrAlert`, `DsfrCallout`, `DsfrTag`, `DsfrLink`, `DsfrBadge`, `DsfrAccordion`, `BandeauPage`, `BriqueHero`, etc.), permettant une personnalisation plus fine sans modifier le code source.
    - Ajout de la propriété `has-no-icon` pour le composant `DsfrBadge`.

### Évolutions techniques
- **Versionning :** Passage à la version majeure 2.0.0.
- **Intégration Svelte :**
    - Restauration de la distribution des composants Svelte dans le dossier `dist/`.
    - Ajout de callbacks Svelte pour les événements WebComponents manquants.
    - Correction de nombreux problèmes d'accès au DOM (notamment via `$host()` et `querySelector`) et de dispatch d'événements spécifiques au mode Svelte.
- **Qualité et Fiabilité :**
    - Déploiement massif de tests automatisés couvrant la quasi-totalité des composants DSFR et Lab pour garantir la stabilité des affichages et des interactions.
- **Architecture :**
    - Optimisation de l'enregistrement des Web Components pour le rendre idempotent (évite les erreurs de double enregistrement des composants Lab ANSSI et DSFR).
    - Unification de l'extraction des métadonnées des Web Components.
- **CI/CD :** Simplification des workflows de test pour Storybook.

### Autres changements
- **Documentation :**
    - Mise à jour des guides concernant les imports CSS pour l'utilisation avec Svelte.
    - Ajout de documentation sur l'amélioration des composants pour le SEO et le SSR (Server-Side Rendering).
    - Mise à jour de la documentation suite à la nouvelle stratégie de distribution des composants.
- **Storybook :** Amélioration de l'interface de développement avec un indicateur visuel pour identifier les composants utilisant des "slots".
