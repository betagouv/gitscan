## Changelog : anssi-portail (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la modernisation de l'interface utilisateur en adoptant les composants du Design System de la République Française (DSFR) sur l'ensemble du site. Des corrections et améliorations ont également été apportées à la gestion des langues, notamment pour la page NIS2, et à la sécurité du site.

### Évolutions fonctionnelles
- **Interface utilisateur :** Migration complète vers les composants DSFR sur toutes les pages du site, améliorant ainsi la cohérence visuelle et l'accessibilité.
- **Page NIS2 :** Ajout de la possibilité de sélectionner la langue (français/anglais) et téléchargement des exigences correspondantes.
- **Filtres :** Correction du fonctionnement des filtres sur les pages Catalogue, Financements et Services.
- **Guides :** Amélioration de l'affichage des images et des assets dans les guides.
- **Connexion :** Mise à jour des liens de connexion pour utiliser les composants DSFR.
- **Statistiques :** Mise à jour de la page des statistiques.

### Évolutions techniques
- **DSFR :** Intégration et utilisation des composants DSFR pour les boutons, les liens, les cartes, les accordéons et autres éléments d'interface.
- **Sécurité :**
    - Mise à jour de plusieurs dépendances pour corriger des vulnérabilités (dompurify, fast-xml-parser, uuid, postcss, follow-redirects).
    - Amélioration de la validation des entrées utilisateur et de l'aseptisation des données.
    - Suppression de l'utilisation de `express-validator` au profit de Zod pour la validation des schémas.
- **Code :**
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Suppression de code inutile et de branches obsolètes.
    - Amélioration du typage des objets validés.
- **Infrastructure :**
    - Configuration de l'accès aux secrets de l'environnement pour les guides.
    - Rendre les bucket des guides configurables.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés.
- **Tests :** Ajout de tests unitaires pour valider les nouvelles fonctionnalités et les corrections de bugs.
- **CI/CD :** Amélioration des workflows CI/CD pour automatiser le processus de déploiement.
- **ESLint :** Ajout d'une règle ESLint pour vérifier l'utilisation de la validation de schéma sur les routes.
- **Accessibilité :** Amélioration de l'accessibilité grâce à l'utilisation des composants DSFR et à la correction de problèmes de CLS (Cumulative Layout Shift).
