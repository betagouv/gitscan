## Changelog : eva-serveur (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur pour les comptes Eva Pro, notamment en refondant le tableau de bord, en améliorant la gestion des structures et des utilisateurs, et en ajoutant des fonctionnalités comme l'invitation de collaborateurs par email. Des corrections de bugs et des améliorations techniques ont également été apportées pour stabiliser et optimiser l'application.

### Évolutions fonctionnelles
- Permet aux utilisateurs de sélectionner un code postal lors de leur inscription [#15a37b1](https://github.com/betagouv/eva-serveur/issues/15a37b1).
- Ajout de la gestion des saisies incomplètes pour les numéros de téléphone français [#7dd1e6f](https://github.com/betagouv/eva-serveur/issues/7dd1e6f).
- Possibilité pour les super-admins d'affecter le même SIRET à plusieurs structures [#0cbb72c](https://github.com/betagouv/eva-serveur/issues/0cbb72c).
- L'utilisateur qui rejoint une entreprise via un lien d'invitation est automatiquement validé [#d9514cc](https://github.com/betagouv/eva-serveur/issues/d9514cc).
- Ajout de la possibilité d'inviter des collègues par email via une modale (DSFR) et l'envoi d'un mail d'invitation [#948bd26](https://github.com/betagouv/eva-serveur/issues/948bd26), [#cbe4044](https://github.com/betagouv/eva-serveur/issues/cbe4044), [#f44d42b](https://github.com/betagouv/eva-serveur/issues/f44d42b).
- Les superadmins peuvent déplacer le dernier admin d'une structure [#993f22a](https://github.com/betagouv/eva-serveur/issues/993f22a).
- Permet aux utilisateurs Evapro de modifier toutes leurs informations [#5eedea3](https://github.com/betagouv/eva-serveur/issues/5eedea3).
- Ajout de la possibilité de télécharger le rapport PDF d'une évaluation pour les comptes Evapro [#2dec6c7](https://github.com/betagouv/eva-serveur/issues/2dec6c7).
- Ajout d'une section "Cinq dernières évaluations" et "Dernière réponse complète" au tableau de bord [#aa53be8](https://github.com/betagouv/eva-serveur/issues/aa53be8), [#5b73e12](https://github.com/betagouv/eva-serveur/issues/5b73e12).
- Ajout de la gestion des SIRET fermés dans la validation des structures [#cf438e8](https://github.com/betagouv/eva-serveur/issues/cf438e8).
- Ajout de la gestion des usages dans le processus d'inscription [#11a485f](https://github.com/betagouv/eva-serveur/issues/11a485f).
- Amélioration de l'affichage et de la gestion des évaluations sur la partie Eva Pro (tableau de bord responsive, correction de bugs d'affichage, etc.) [#3c84d6e](https://github.com/betagouv/eva-serveur/issues/3c84d6e), [#5678f6b](https://github.com/betagouv/eva-serveur/issues/5678f6b), [#ff3c3a5](https://github.com/betagouv/eva-serveur/issues/ff3c3a5), [#dee501b](https://github.com/betagouv/eva-serveur/issues/dee501b), [#09219c2](https://github.com/betagouv/eva-serveur/issues/09219c2), [#4b79713](https://github.com/betagouv/eva-serveur/issues/4b79713), [#6b0d06d](https://github.com/betagouv/eva-serveur/issues/6b0d06d).

### Évolutions techniques
- Refonte du header et de la navigation avec le DSFR pour une meilleure expérience utilisateur et une cohérence visuelle [#9012a2d](https://github.com/betagouv/eva-serveur/issues/9012a2d), [#59831a2](https://github.com/betagouv/eva-serveur/issues/59831a2).
- Suppression de la relation many-to-many entre Structures et Opcos, simplification en une relation one-to-one [#728f9ac](https://github.com/betagouv/eva-serveur/issues/728f9ac).
- Ajout d'un composant `BoutonDsfr` pour une gestion plus cohérente des boutons [#297bdfe](https://github.com/betagouv/eva-serveur/issues/297bdfe).
- Mise à jour du DSFR de la version 1.13.0 à la version 1.14.2 [#2712418](https://github.com/betagouv/eva-serveur/issues/2712418).
- Ajout d'un linter pour vérifier la présence d'espaces insécables [#d0f0008](https://github.com/betagouv/eva-serveur/issues/d0f0008).
- Amélioration de la CI et mise à jour de Guard [#4691b96](https://github.com/betagouv/eva-serveur/issues/4691b96), [#83f4ccb](https://github.com/betagouv/eva-serveur/issues/83f4ccb).
- Ajout de tests pour l'invitation par email [#88da7dd](https://github.com/betagouv/eva-serveur/issues/88da7dd).
- Suppression de code inutile et refactoring du code pour une meilleure maintenabilité [#25fdf4d](https://github.com/betagouv/eva-serveur/issues/25fdf4d), [#edda441](https://github.com/betagouv/eva-serveur/issues/edda441), [#38317d4](https://github.com/betagouv/eva-serveur/issues/38317d4).

### Autres changements
- Ajout de logos dans un dossier dédié [#b879a18](https://github.com/betagouv/eva-serveur/issues/b879a18).
- Correction de typos et amélioration de la lisibilité du code [#394a2a6](https://github.com/betagouv/eva-serveur/issues/394a2a6), [#9d5cd08](https://github.com/betagouv/eva-serveur/issues/9d5cd08).
- Ajout de questionnaires supplémentaires pour Bienvenue, pour l'option des questions de santé [#797c4e3](https://github.com/betagouv/eva-serveur/issues/797c4e3).
- Suppression de la configuration mailjet pour le tracking [#9ab6c80](https://github.com/betagouv/eva-serveur/issues/9ab6c80).
- Ajout d'un feature flag pour activer/désactiver Evapro [#c2d0275](https://github.com/betagouv/eva-serveur/issues/c2d0275).
- Diverses corrections de style et d'accessibilité.
- Mise à jour de certaines dépendances (nokogiri, rack, faraday).
