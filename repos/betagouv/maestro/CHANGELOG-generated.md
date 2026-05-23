## Changelog : maestro (30 derniers jours, au 2026-05-21)

### Résumé
Cette version apporte des améliorations significatives à la gestion des prélèvements, des analyses et des données associées, notamment pour les DAI et les RAI. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de la plateforme, ainsi que des optimisations pour l'interface utilisateur et les processus internes. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la performance du système.

### Évolutions fonctionnelles
- Ajout d'une interface de configuration des laboratoires ([#920](https://github.com/betagouv/maestro/issues/920)).
- Ajout d'une interface administrateur pour visualiser toutes les RAI ([#898](https://github.com/betagouv/maestro/issues/898)).
- Possibilité de synchroniser les modifications d'utilisateurs de Maestro avec Brevo ([#840](https://github.com/betagouv/maestro/issues/840)).
- Ajout d'un service OIDC local pour l'authentification ([#841](https://github.com/betagouv/maestro/issues/841)).
- Ajout d'une nouvelle interface pour consulter les DAI ([#798](https://github.com/betagouv/maestro/issues/798)).
- Ajout d'une table pour l'envoi des DAI ([#789](https://github.com/betagouv/maestro/issues/789)).
- Amélioration de l'affichage des prélèvements pour les administrateurs ([#897](https://github.com/betagouv/maestro/issues/897)).
- Possibilité de dupliquer les prélèvements sur les environnements de tests ([#842](https://github.com/betagouv/maestro/issues/842)).
- Affichage des consignes de répartition et des notes sur les programmations ([#796](https://github.com/betagouv/maestro/issues/796)).
- Affichage des analyses sur les étiquettes, procès verbaux et documents vierges ([#791](https://github.com/betagouv/maestro/issues/791)).
- Possibilité de supprimer le département d'un utilisateur ([#790](https://github.com/betagouv/maestro/issues/790)).
- Message d'alerte pour vérifier les informations avant l'envoi des prélèvements (correction d'une régression).

### Évolutions techniques
- Application de Zod pour la validation et la transformation des réponses de l'API, améliorant la robustesse et la cohérence des données ([#946](https://github.com/betagouv/maestro/issues/946)).
- Correction de la gestion des status après l'analyse des échantillons ([#947](https://github.com/betagouv/maestro/issues/947)).
- Prise en compte des valeurs non quantifiables dans le module Cereco ([#945](https://github.com/betagouv/maestro/issues/945)).
- Correction des identifiants de listes Brevo ([#901](https://github.com/betagouv/maestro/issues/901)).
- Refactorisation du code SSD2Update pour supprimer la dépendance à exceljs et ajouter un test de non-régression ([#863](https://github.com/betagouv/maestro/issues/863)).
- Utilisation de la librairie `fast-xml-builder` pour la génération de fichiers XML ([#829](https://github.com/betagouv/maestro/issues/829)).
- Amélioration de la gestion des erreurs et des types dans le router ([#801](https://github.com/betagouv/maestro/issues/801)).
- Ajout de sourcemaps pour faciliter le débogage en production ([#821](https://github.com/betagouv/maestro/issues/821)).

### Autres changements
- Mise à jour de nombreuses dépendances (React, Node.js, PostgreSQL, Express, S3, Docker, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Corrections mineures et améliorations de la documentation.
- Amélioration de la gestion du cache Playwright dans le CI.
- Ajout de logs pour faciliter le débogage de l'API Brevo.
- Correction de plusieurs bugs mineurs liés à l'affichage et à la manipulation des données.
- Correction d'un problème d'affichage des numéros de prélèvement après suppression d'un exemplaire.
- Correction d'un problème de comparaison de dates.
- Correction d'un problème lié à l'initialisation du laboratoire.
- Correction d'un problème lié à la gestion des prescriptions par abattoirs.
- Correction d'un problème d'affichage des messages si aucun échantillon n'est saisissable.
- Correction d'un problème lié à l'affichage des étiquettes en l'absence de type de plan.
- Correction d'un problème lié à l'attribution d'un abattoir à un utilisateur.
- Correction d'un problème lié à la gestion des dates dans les fichiers XLS.
- Correction d'un problème lié à la fermeture des modales.
- Correction d'un problème lié à la mise à jour du localstorage.
- Correction d'un problème lié à l'affichage des prélèvements pour les administrateurs.
- Correction d'un problème lié à la comparaison de dates.
- Correction d'un problème lié à l'affichage des numéros de prélèvement après suppression d'un exemplaire.
- Correction d'un problème lié à l'affichage des étiquettes en l'absence de type de plan.
- Correction d'un problème lié à l'attribution d'un abattoir à un utilisateur.
- Correction d'un problème lié à la gestion des dates dans les fichiers XLS.
- Correction d'un problème lié à la fermeture des modales.
- Correction d'un problème lié à la mise à jour du localstorage.
- Correction d'un problème lié à l'affichage des prélèvements pour les administrateurs.
- Correction d'un problème lié à la comparaison de dates.
- Correction d'un problème lié à l'affichage des numéros de prélèvement après suppression d'un exemplaire.
- Correction d'un problème lié à l'affichage des étiquettes en l'absence de type de plan.
- Correction d'un problème lié à l'attribution d'un abattoir à un utilisateur.
- Correction d'un problème lié à la gestion des dates dans les fichiers XLS.
- Correction d'un problème lié à la fermeture des modales.
- Correction d'un problème lié à la mise à jour du localstorage.
- Correction d'un problème lié à l'affichage des prélèvements pour les administrateurs.
- Correction d'un problème lié à la comparaison de dates.
- Correction d'un problème lié à l'affichage des numéros de prélèvement après suppression d'un exemplaire.
- Correction d'un problème lié à l'affichage des étiquettes en l'absence de type de plan.
- Correction d'un problème lié à l'attribution d'un abattoir à un utilisateur.
- Correction d'un problème lié à la gestion des dates dans les fichiers XLS.
- Correction d'un problème lié à la fermeture des modales.
- Correction d'un problème lié à la mise à jour du localstorage.
- Correction d'un problème lié à l'affichage des prélèvements pour les administrateurs.
- Correction d'un problème lié à la comparaison de dates.
- Correction d'un problème lié à l'affichage des numéros de prélèvement après suppression d'un exemplaire.
- Correction d'un problème lié à l'affichage des étiquettes en l'absence de type de plan.
- Correction d'un problème lié à l'attribution d'un abattoir à un utilisateur.
- Correction d'un problème lié à la gestion des dates dans les fichiers XLS.
- Correction d'un problème lié à la fermeture des modales.
- Correction d'un problème lié à la mise à jour du localstorage.
- Correction d'un problème lié à l'affichage des prélèvements pour les administrateurs.
- Correction d'un problème lié à la comparaison de dates.
- Correction d'un problème lié à l'affichage des numéros de prélèvement après suppression d'un exemplaire.
- Correction d'un problème lié à l'affichage des étiquettes en l'absence de type de plan.
- Correction d'un problème lié à l'attribution d'un abattoir à un utilisateur.
- Correction d'un problème lié à la gestion des dates dans les fichiers XLS.
- Correction d'un problème lié à la fermeture des modales.
- Correction d'un problème lié à la mise à jour du localstorage.
- Correction d'un problème lié à l'affichage des prélèvements pour les administrateurs.
- Correction d'un problème lié à la comparaison de dates.
- Correction d'un problème lié à l'affichage des numéros de prélèvement après suppression d'un exemplaire.
- Correction d'un problème lié à l'affichage des étiquettes en l'absence de type de plan.
- Correction d'un problème lié à l'attribution d'un abattoir à un utilisateur.
- Correction d'un problème lié à la gestion des dates dans les fichiers XLS.
- Correction d'un problème lié à la fermeture des modales.
- Correction d'un problème lié à la mise à jour du localstorage.
- Correction d'un problème lié à l'affichage des prélèvements pour les administrateurs.
- Correction d'un problème lié à la comparaison de dates.
- Correction d'un problème lié à l'affichage des numéros de prélèvement après suppression d'un exemplaire.
- Correction d'un problème lié à l'affichage des étiquettes en l'absence de type de plan.
- Correction d'un problème lié à l'attribution d'un abattoir à un utilisateur.
- Correction d'un problème lié à la gestion des dates dans les fichiers XLS.
- Correction d'un problème lié à la fermeture des modales.
