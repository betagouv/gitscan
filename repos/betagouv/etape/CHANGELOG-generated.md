## Changelog : etape (30 derniers jours, au 31 juillet 2026)

### Résumé
Le projet a franchi une étape majeure avec l'intégration de la page d'accueil et la mise en place opérationnelle du simulateur d'éligibilité. L'accent a été mis sur la cohérence visuelle avec les maquettes, l'accessibilité (navigation clavier, liens d'évitement) et la mise en place d'une structure technique robuste pour supporter l'évolution du produit.

### Évolutions fonctionnelles
- **Intégration du site vitrine** : Mise en ligne de la page d'accueil avec son contenu éditorial, ses visuels et un design responsive adapté à tous les écrans. [#10](https://github.com/betagouv/etape/pull/10)
- **Développement du simulateur** : Implémentation du parcours utilisateur du questionnaire, incluant l'écran d'introduction, la gestion des questions et une page d'erreur. [#7](https://github.com/betagouv/etape/pull/7) [#3](https://github.com/betagouv/etape/pull/3)
- **Amélioration de l'expérience utilisateur** : Ajout d'une confirmation de sortie lors du questionnaire, amélioration de la navigation arrière et ajout d'un bouton de retour en haut de page.
- **Navigation et accessibilité** : Mise en place d'un pied de page, d'un menu mis à jour et de liens d'évitement (SkipLinks) pour faciliter la navigation au clavier. [#8](https://github.com/betagouv/etape/pull/8)

### Évolutions techniques
- **Architecture Monorepo** : Initialisation de la structure avec Turborepo pour gérer conjointement le site vitrine et l'application simulateur.
- **Design System partagé** : Création d'un package UI centralisant les composants fondamentaux (boutons, cartes, sections, conteneurs, gestion du focus clavier) et l'échelle typographique.
- **UI & Styling** : Intégration de Shadcn UI et alignement rigoureux des composants et des espacements sur les maquettes Figma.
- **CI/CD** : Configuration des déploiements de prévisualisation (previews) sur Vercel en mode "prebuilt". [#9](https://github.com/betagouv/etape/pull/9)
- **Qualité de code** : Mise en place d'une configuration centralisée et partagée pour ESLint et Prettier. [#2](https://github.com/betagouv/etape/pull/2)

### Autres changements
- **Documentation** : Ajout d'un template de Pull Request pour standardiser les contributions.
- **Configuration** : Mise à jour des fichiers `.gitignore` et nettoyage des commentaires de code superflus.
