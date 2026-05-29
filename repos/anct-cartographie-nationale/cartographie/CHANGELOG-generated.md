## Changelog : cartographie (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, la cartographie a bénéficié d'améliorations significatives, notamment l'ajout d'un formulaire de contact complet avec envoi d'emails, des optimisations de performance pour l'affichage des horaires d'ouverture des lieux, et des corrections pour assurer la stabilité et la fiabilité de l'application. Des améliorations de l'infrastructure et de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un formulaire de contact avec envoi d'emails via Brevo (SMTP) : les utilisateurs peuvent désormais contacter l'équipe directement depuis l'application. [#fca7f7d](https://github.com/anct-cartographie-nationale/cartographie/commit/fca7f7d15e4b6be20ece4a2b7c6fe384047f2752)
- Amélioration de l'expérience utilisateur du formulaire de contact : interface plus claire et informations supplémentaires sur l'aide disponible. [#379c192](https://github.com/anct-cartographie-nationale/cartographie/commit/379c192795998d4e2df3fc1cbb3a19be3d728f7c)
- Ajout de filtres pour afficher les lieux ouverts actuellement ou pendant le week-end. [#5e43199](https://github.com/anct-cartographie-nationale/cartographie/commit/5e4319967241794588547f55389891b7a2868849)
- Ajout d'un bouton pour intégrer la carte sur d'autres sites web. [#c339f1b](https://github.com/anct-cartographie-nationale/cartographie/commit/c339f1b554288466659b79f11747a23977529623)
- Amélioration de l'affichage du label "Site internet" sur la page de détail d'un lieu. [#2ae2aff](https://github.com/anct-cartographie-nationale/cartographie/commit/2ae2aff0b4780464f2096045f521996798654691)

### Évolutions techniques
- Optimisation des performances : chargement paresseux de l'analyse des horaires d'ouverture et filtrage en deux passes. [#4f7f332](https://github.com/anct-cartographie-nationale/cartographie/commit/4f7f332b940c39b0a8479776ddabf64f2d446961)
- Mise à jour de l'infrastructure SMTP : passage de Scaleway TEM à Brevo via Secret Manager pour une meilleure gestion des identifiants. [#63bdff7](https://github.com/anct-cartographie-nationale/cartographie/commit/63bdff79561f95b728249356609645f45497f048)
- Mise à jour de pnpm à la version 11 et configuration de Node.js avant pnpm. [#2672b3e](https://github.com/anct-cartographie-nationale/cartographie/commit/2672b3e1886036461589116f7439228284a4751f)
- Amélioration de la sécurité : ajout de la détection de secrets avec Gitleaks dans le pre-commit hook et le CI. [#f24c364](https://github.com/anct-cartographie-nationale/cartographie/commit/f24c364946286a391971916f49216f279462974b)
- Correction d'un problème de gestion des paramètres de requête `territoire_type`. [#d37f489](https://github.com/anct-cartographie-nationale/cartographie/commit/d37f489f47a749880b1331676846b61d47057122)

### Autres changements
- Mise à jour des dépendances (Next.js, Pulumi, etc.).
- Ajout de configuration Dependabot pour la gestion des dépendances npm et des actions GitHub.
- Mise à jour de la documentation et des textes d'introduction du formulaire de contact.
- Ajout de Mailpit pour faciliter les tests SMTP en local.
- Corrections mineures et refactoring du code.
