## Changelog : nosgestesclimat-site-nextjs (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'expérience utilisateur en simplifiant certaines fonctionnalités, en corrigeant des bugs et en optimisant le suivi des données. Des améliorations ont été apportées aux pages d'organisation, aux résultats détaillés, et à la gestion des cookies. L'application a également été mise à jour avec la dernière version du modèle de calcul d'empreinte carbone.

### Évolutions fonctionnelles
- Possibilité pour les membres d'un groupe ou d'une organisation de créer un compte directement depuis l'interface dédiée. [#1639](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1639)
- Ajout d'une bannière pour inviter les utilisateurs à consulter les résultats de leur groupe. [#1663](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1663)
- Nouvelle section "Objectifs" sur la page des résultats. [#1661](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1661)
- Nouvelle composante affichant les résultats par catégorie. [#1641](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1641)
- Bloc "Sauvegarder la simulation" ajouté. [#1653](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1653)
- Amélioration de la formulation sur la page de connexion des organisations et ajout de la mention "animateurs". [#1667](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1667), [#1668](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1668)
- Correction d'un bug empêchant les utilisateurs de modifier leur adresse e-mail. [#1689](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1689)
- Correction d'un bug empêchant la désélection d'éléments. [#1646](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1646)

### Évolutions techniques
- Mise à jour du modèle de calcul d'empreinte carbone vers la version 4.9.1 et 4.9.0. [#1664](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1664), [#1652](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1652)
- Amélioration du suivi des événements PostHog et de la gestion des cookies. [#1693](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1693), [#1662](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1662), [#1654](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1654)
- Refactorisation du code et suppression de fonctionnalités obsolètes (Tally NPS form, water bloc, email field dans les paramètres de l'organisation). [#1695](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1695), [#1694](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1694), [#1692](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1692), [#1690](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1690)
- Configuration du nom du cookie d'authentification via une variable d'environnement. [#1666](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1666)
- Correction d'un problème de crash de l'application Scalingo dû à une dépendance TypeScript. [#1651](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1651)

### Autres changements
- Mise à jour de la documentation README et du fichier .gitignore. [#1684](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1684)
- Amélioration des traductions anglaises. [#1688](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1688)
- Suppression du bloc Microsoft email. [#1640](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1640)
- Correction de l'état d'acceptation des cookies GTM pour les utilisateurs de retour. [#1682](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1682)
- Suppression des hreflang pour les pages Strapi en français uniquement. [#1680](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1680)
- Mise à jour du chemin du service worker mock. [#1678](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1678)
- Correction d'une faute de frappe dans un script. [#1677](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1677)
- Amélioration de l'angle et de la longueur de la flèche sur la page de fin. [#1671](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1671)
- Ajout de tracking pour le clic "renvoyer le code".
