## Changelog : depots-sauvages (30 derniers jours, au 06 août 2026)

### Résumé
L'application s'enrichit de nouveaux outils pour mieux accompagner les utilisateurs, notamment via l'ajout de pages d'information et de mécanismes de recueil de satisfaction. Parallèlement, une infrastructure de statistiques a été mise en place pour permettre un meilleur suivi de l'activité, tandis que l'expérience utilisateur et la sécurité ont été renforcées.

### Évolutions fonctionnelles
- **Recueil de feedback** : Mise en place de formulaires d'utilisabilité et de popups (Tally) pour mesurer la satisfaction des utilisateurs en fin de procédure ([#202](https://github.com/betagouv/depots-sauvages/issues/202), [#204](https://github.com/betagouv/depots-sauvages/issues/204)).
- **Nouvelles pages et navigation** : Création de la page "Comment agir" et refonte de la page dédiée aux webinaires ([#194](https://github.com/betagouv/depots-sauvages/issues/194)).
- **Amélioration de l'expérience utilisateur (UX)** : Simplification du parcours de constatation ([#196](https://github.com/betagouv/depots-sauvages/issues/196)), optimisation de la page d'accueil ([#199](https://github.com/betagouv/depots-sauvages/issues/199)) et amélioration de la visualisation des cartes de procédures ([#201](https://github.com/betagouv/depots-sauvages/issues/201)).
- **Mises à jour des contenus** : Actualisation des informations de contact ([#205](https://github.com/betagouv/depots-sauvages/issues/205)), corrections orthographiques et de clarté ([#200](https://github.com/betagouv/depots-sauvages/issues/200)), ajustements de la terminologie ([#212](https://github.com/betagouv/depots-sauvages/issues/212)) et ajout d'informations sur le nettoyage des dépôts ([#193](https://github.com/betagouv/depots-sauvages/issues/193)).
- **Gestion administrative** : Correctifs dans le backoffice concernant les observations des collectivités et le suivi du nettoyage ([#190](https://github.com/betagouv/depots-sauvages/issues/190)).

### Évolutions techniques
- **Module de statistiques** : Implémentation d'une base de données dédiée, gestion des migrations et automatisation via des tâches planifiées (cron jobs) pour le suivi des données ([#206](https://github.com/betagouv/depots-sauvages/issues/206), [#209](https://github.com/betagouv/depots-sauvages/issues/209), [#210](https://github.com/betagouv/depots-sauvages/issues/210)).
- **Sécurité et traçabilité** : Renforcement de la sécurité du système ([#195](https://github.com/betagouv/depots-sauvages/issues/195)) et ajout de logs d'activité ([#213](https://github.com/betagouv/depots-sauvages/issues/213)).
- **Maintenance et refactorisation** : Optimisation du code sur la page "Comment agir" ([#198](https://github.com/betagouv/depots-sauvages/issues/198)), renommage d'une librairie ([#191](https://github.com/betagouv/depots-sauvages/issues/191)) et corrections diverses d'imports et de styles ([#211](https://github.com/betagouv/depots-sauvages/issues/211)).

### Autres changements
- **Référencement** : Optimisation du SEO par la correction des titres et descriptions des pages clés ([#203](https://github.com/betagouv/depots-sauvages/issues/203)).
