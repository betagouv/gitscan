## Changelog : lab-anssi-ui-kit (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante de mise en conformité avec le DSFR pour l'ensemble des composants de la bibliothèque "LAB". Les efforts se sont concentrés sur l'amélioration de l'accessibilité, la réactivité des composants et une montée de version majeure de l'outil de build (Vite 8) pour garantir des performances et une sécurité optimales.

### Évolutions fonctionnelles
- **Nouveautés** : Ajout du composant `DsfrTooltip`.
- **Mise en conformité DSFR** : Alignement structurel et stylistique des composants du LAB (`LabAnssiFonctionnalites`, `LabAnssiCentreAide`, `LabAnssiSuiteCyber`, `LabAnssiBandeauPage`, `LabAnssiCarrouselTuiles` et `LabAnssiMarelle`) sur les standards du design system.
- **Accessibilité et UX** : 
    - Amélioration de la navigation et des rôles ARIA pour `Alerte`, `DsfrRadiosGroup` et `DsfrCheckboxesGroup`.
    - Ajout du support `prefers-reduced-motion` et d'un bouton de pause pour le composant `LabAnssiFonctionnalites`.
    - Amélioration de la gestion des icônes et des slots (notamment pour `DsfrToggle` et `DsfrCard`).
- **Réactivité et synchronisation** : Optimisation de la réactivité des états et de la synchronisation des données pour de nombreux composants (`DsfrDropdown`, `MultiSelect`, `DsfrSegmented`, `DsfrTable`, `DsfrTranslate`, `LienDiagnosticCyber`, etc.).
- **Personnalisation** : Extension des options de personnalisation (thèmes, couleurs, z-index et breakpoints) pour les composants `LabAnssiBandeauPage`, `LabAnssiSuiteCyber` et `DsfrHeader`.

### Évolutions techniques
- **Build & Tooling** : 
    - Migration vers la version majeure **Vite 8**, incluant le passage aux modules ESM et la correction de l'injection du nonce CSP.
    - Réorganisation des stories Storybook (déplacement des composants LAB vers un dossier legacy).
- **Infrastructure & CI/CD** : 
    - Optimisation des politiques de cache et correction des types MIME lors de l'envoi des fichiers vers S3.
    - Consolidation de la configuration `pnpm`.
    - Ajustement des règles de mise à jour des dépendances (instauration d'une période de publication minimale de 7 jours).

### Autres changements
- **Documentation** : Corrections de l'affichage des couleurs dans la documentation technique.
- **Formatage** : Mise à jour du formatage global du code suite à la montée de version de Prettier.
