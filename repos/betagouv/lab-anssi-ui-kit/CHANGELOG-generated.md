## Changelog : lab-anssi-ui-kit (30 derniers jours, au 04/09/2026)

### Résumé
Cette période a été marquée par une montée en version majeure de l'infrastructure de build (Vite 8) et un effort important de mise en conformité avec le DSFR pour les composants du Lab ANSSI. Les améliorations se sont concentrées sur la réactivité des composants, l'accessibilité (gestion du focus, réduction de mouvement) et la robustesse des interfaces pour les produits du Lab.

### Évolutions fonctionnelles
- **Accessibilité et expérience utilisateur** :
    - Amélioration de la visibilité du focus pour la navigation au clavier.
    - Ajout de noms explicites sur les boutons de fermeture (ex: composant Alerte) pour les lecteurs d'écran.
    - Suppression de rôles ARIA redondants sur les groupes de boutons radio et de cases à cocher.
    - Support du mode "réduction de mouvement" (`prefers-reduced-motion`) et ajout d'un bouton de pause pour les animations de défilement (composant `LabAnssiFonctionnalités`).
    - Documentation des éléments interactifs (tags pressables).
- **Améliorations des composants Lab ANSSI** :
    - `LabAnssiFonctionnalités` : Ajout de slots pour personnaliser les zones d'illustration (médias), gestion du défilement au survol et nouvelles propriétés de style.
    - `LabAnssiCentreAide` : Mise en conformité avec le DSFR, ajustement de la taille des éléments selon la résolution d'écran et gestion optimisée des superpositions (z-index).
    - `SuiteCyber` : Mise en conformité structurelle avec le DSFR et correction de l'affichage sur mobile.
    - `LabAnssiCarrouselTuiles` : Ajustement des points de rupture (breakpoints) et rendu des propriétés de contenu optionnelles.
- **Nouvelles fonctionnalités et flexibilité** :
    - Ajout de slots pour personnaliser le pied de page de `DsfrModal`, la navigation de `DsfrHeader` et les aides de `DsfrToggle`.
    - Possibilité de masquer l'icône sur le composant `DsfrCard`.
    - Ajustement de la taille de l'icône de lien (`DsfrLink`) selon la variation de texte.
- **Réactivité et synchronisation** :
    - Amélioration de la synchronisation des données pour de nombreux composants : `DsfrTable` (pagination), `MultiSelect` (valeurs sélectionnées), `DsfrSegmented` (valeur active), `DsfrTranslate` (langue active) et `ListeArticles`.

### Évolutions techniques
- **Infrastructure et Build** :
    - Migration majeure vers **Vite 8**.
    - Passage des configurations Vite vers le format ESM (remplacement des patterns CommonJS).
    - Correction de l'injection du nonce CSP pour le nouveau format de sortie de Vite.
- **Qualité et Outillage** :
    - Consolidation de la configuration `pnpm`.
    - Mise à jour du formatage du code via Prettier.
    - Amélioration des stories Storybook pour garantir une conformité stricte au DSFR.
    - Nettoyage des blocs de code et effets "legacy" dans plusieurs composants.
- **Déploiement** :
    - Optimisation des politiques de cache lors de l'envoi des assets vers S3.
    - Correction de types MIME dans les scripts de déploiement.

### Autres changements
- Ajout d'icônes manquantes (gamepad).
- Mise à jour de la documentation concernant le processus de release.
