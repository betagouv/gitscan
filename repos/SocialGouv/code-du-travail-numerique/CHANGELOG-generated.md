## Changelog : code-du-travail-numerique (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche, la gestion de la conformité RGPD, et la correction de bugs pour une meilleure expérience utilisateur. L'ajout d'une section actualités enrichit également le contenu proposé. Des améliorations techniques ont été apportées, notamment la migration des tests E2E vers Playwright.

### Évolutions fonctionnelles
- **Recherche :** Mise en place d'un A/B testing sur les labels pour les contributions, afin d'optimiser la pertinence des résultats. [#7243](https://github.com/SocialGouv/code-du-travail-numerique/issues/7243)
- **RGPD :** Ajout d'un avertissement lors de la saisie de données personnelles dans les commentaires, pour sensibiliser les utilisateurs. [#7244](https://github.com/SocialGouv/code-du-travail-numerique/issues/7244)
- **RGPD :** Mise à jour du bandeau cookie pour assurer la conformité. [#7248](https://github.com/SocialGouv/code-du-travail-numerique/issues/7248)
- **Actualités :** Ajout d'une page listant les actualités, enrichissant l'offre d'information. [#7205](https://github.com/SocialGouv/code-du-travail-numerique/issues/7205)
- **Outils :** Ajout d'une illustration du bulletin de paie sur le préavis de démission, pour une meilleure compréhension. [#7210](https://github.com/SocialGouv/code-du-travail-numerique/issues/7210)
- **Indemnité de licenciement :** Suppression de la question sur la date de sortie pour la convention collective 3239. [#7236](https://github.com/SocialGouv/code-du-travail-numerique/issues/7236)
- **Modèles de courrier :** Changement du breakpoint entre `md` et `lg` pour une meilleure adaptation sur différents écrans. [#7197](https://github.com/SocialGouv/code-du-travail-numerique/issues/7197)
- **Contributions :** Redirection automatique vers la convention collective une fois celle-ci sauvegardée dans le header. [#7203](https://github.com/SocialGouv/code-du-travail-numerique/issues/7203)

### Évolutions techniques
- **Tests E2E :** Migration des tests E2E de Cypress vers Playwright, améliorant la fiabilité et la performance des tests. [#7212](https://github.com/SocialGouv/code-du-travail-numerique/issues/7212)
- **Recherche :** Corrections sur l'affichage des résultats de recherche. [#7219](https://github.com/SocialGouv/code-du-travail-numerique/issues/7219)
- **Sentry :** Correction des erreurs remontées par Sentry, améliorant la stabilité de l'application. [#7225](https://github.com/SocialGouv/code-du-travail-numerique/issues/7225)
- **pnpm :** Mise à jour de pnpm. [#7193](https://github.com/SocialGouv/code-du-travail-numerique/issues/7193)

### Autres changements
- **Recherche :** Renommage des labels pour les contributions et les autres pages. [#7227](https://github.com/SocialGouv/code-du-travail-numerique/issues/7227)
- **Actualités :** Ajout de la source des actualités. [#7204](https://github.com/SocialGouv/code-du-travail-numerique/issues/7204)
- **Recherche :** Correction d'un mismatch dans la recherche des définitions. [#7206](https://github.com/SocialGouv/code-du-travail-numerique/issues/7206)
- **Thème :** Utilisation de `focusable` à `false` sur les icônes pour améliorer l'accessibilité. [#7192](https://github.com/SocialGouv/code-du-travail-numerique/issues/7192)
- **Recherche :** Modification du wording pour le moteur de recherche. [#7191](https://github.com/SocialGouv/code-du-travail-numerique/issues/7191)
- **Quoi de neuf :** Ajout du message "Aucune actualité cette semaine" lorsque aucune actualité n'est disponible. [#7198](https://github.com/SocialGouv/code-du-travail-numerique/issues/7198)
- **Modale :** Corrections des derniers retours UI sur la modale. [#7194](https://github.com/SocialGouv/code-du-travail-numerique/issues/7194)
- **Events :** Suppression de l'event qui track l'input `agreement search`. [#7200](https://github.com/SocialGouv/code-du-travail-numerique/issues/7200)
- **Recherche :** Correction de l'IDCCXXXX pattern et ajout de la classe siret. [#7216](https://github.com/SocialGouv/code-du-travail-numerique/issues/7216)
- **Actualités :** Corrections sur les titres, les marges et bug sur les liens. [#7218](https://github.com/SocialGouv/code-du-travail-numerique/issues/7218)
- **Recherche :** Mise en place de la masonry grid layout en horizontal. [#7215](https://github.com/SocialGouv/code-du-travail-numerique/issues/7215)
