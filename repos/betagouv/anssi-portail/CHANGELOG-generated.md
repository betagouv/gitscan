## Changelog : anssi-portail (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'intégration du Design System de la République Française (DSFR) pour une interface plus cohérente et accessible. Le simulateur NIS2 a été considérablement enrichi avec l'ajout de nouvelles étapes et fonctionnalités, et une fonctionnalité d'abonnement à une newsletter a été implémentée. Des corrections de sécurité et des améliorations de la gestion des guides ont également été apportées.

### Évolutions fonctionnelles
- **Simulateur NIS2 :** Ajout de nombreuses étapes au simulateur (localisation des services numériques, type de structure, appartenance UE, etc.) et intégration d'une étape de résultat. Possibilité de tester l'éligibilité à NIS2.
- **Newsletter :** Implémentation d'un formulaire d'abonnement à une newsletter avec validation et intégration à Brevo. Ajout d'une page de confirmation d'abonnement.
- **Gestion des guides :**
    - Possibilité de copier le lien court d'un guide.
    - Ajout d'une étape d'approbation pour les guides.
    - Amélioration de la gestion des documents associés aux guides (ajout, suppression, affichage).
    - Génération automatique de visuels pour les guides.
- **Interface utilisateur :**
    - Migration de nombreux composants vers le Design System de la République Française (DSFR) pour une meilleure cohérence visuelle et accessibilité.
    - Amélioration de l'apparence des cartes et des boutons.
    - Ajout de liens DSFR.
- **Recherche :** Adaptation de la recherche d'entreprise.

### Évolutions techniques
- **Sécurité :**
    - Mise à jour de plusieurs dépendances pour corriger des vulnérabilités (dompurify, fast-xml-parser, uuid, postcss, follow-redirects).
    - Validation des entrées utilisateurs avec Zod pour renforcer la sécurité.
    - Suppression de l'utilisation de `express-validator`.
- **Infrastructure :**
    - Mise à jour de Sentry pour la gestion des erreurs.
    - Amélioration de la gestion des variables d'environnement.
- **Code :**
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Utilisation de TypeScript pour un typage plus strict.
    - Suppression de code inutile.
    - Amélioration du formattage du code.
    - Ajout de tests unitaires et d'intégration.

### Autres changements
- Ajout de documentation.
- Correction de bugs mineurs.
- Amélioration des messages d'erreur.
- Mise à jour de la configuration du projet.
- Ajout de sourcemaps pour Sentry.
- Correction de l'étirement des images SVG.
- Ajout de métadonnées SEO (descriptions, attributs alt).
- Mise à jour de la version de l'UI Kit.
- Ajout de commentaires et de documentation au code.
