## Changelog : anssi-portail (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des guides (affichage, gestion des versions, liens) et de l'accessibilité. De nombreuses mises à jour techniques ont également été effectuées pour moderniser le code, améliorer la sécurité et optimiser les performances, avec une migration vers les composants DSFR.

### Évolutions fonctionnelles
- **Guides :**
    - Ajout de la possibilité de copier le lien court d'un guide.
    - Amélioration de l'affichage des guides, notamment l'espacement et l'harmonisation mobile/bureau.
    - Gestion des anciens documents et des liens associés.
    - Ajout d'une étape d'approbation pour les guides.
    - Affichage d'un encart informatif sur les guides.
- **Interface utilisateur :**
    - Mise à jour de nombreux composants pour utiliser la bibliothèque DSFR, améliorant la cohérence visuelle et l'accessibilité.
    - Amélioration de la navigation avec l'affichage de l'élément de navigation courant.
    - Correction de problèmes d'étirement des images.
    - Ajout de liens d'évitement (skiplinks) pour une meilleure accessibilité.
    - Amélioration de l'affichage des filtres actifs dans la section financements.
- **NIS2 :**
    - Ajout de la possibilité de sélectionner la langue (français/anglais) pour les exigences NIS2.
    - Traduction des exports CSV pour les exigences NIS2.
    - Ajout de la documentation NIS2 en téléchargement.
- **Recherche :**
    - Préparation d'un adaptateur pour la recherche d'entreprises.
- **Autres :**
    - Mise à jour de la page des statistiques.

### Évolutions techniques
- **Architecture & Composants :**
    - Migration vers les composants DSFR pour l'ensemble de l'interface utilisateur (boutons, liens, accordéons, cartes, etc.).
    - Refonte de la gestion des liens pour utiliser les composants DSFR.
    - Suppression de code obsolète (ancien accordéon, styles CSS inutiles).
- **Sécurité :**
    - Mise à jour de plusieurs dépendances pour corriger des vulnérabilités (axios, dompurify, uuid, postcss).
    - Validation des entrées utilisateur avec Zod pour renforcer la sécurité.
    - Suppression de l'utilisation de `express-validator`.
    - Aseptisation des chaines de caractères utilisées dans les attributs HTML.
- **Performance & Infrastructure :**
    - Suppression de la mise en cache pour les guides.
    - Amélioration de la gestion des ressources et des secrets.
    - Optimisation du code pour réduire le CLS (Cumulative Layout Shift).
- **Développement :**
    - Mise à jour des versions de l'UI Kit.
    - Amélioration des tests et de la qualité du code.
    - Utilisation de sourcemaps pour Sentry.

### Autres changements
- Documentation mise à jour.
- Suppression de branches inutiles.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Ajout de règles ESLint pour renforcer la cohérence du code.
- Mise à jour des métadonnées SEO (descriptions, attributs alt).
