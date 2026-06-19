## Changelog : monlogementetudiant (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment avec l'ajout d'alertes CROUS sur la page d'accueil, des améliorations de la recherche et de la gestion des propriétaires. Des corrections et des optimisations ont également été apportées pour améliorer la fiabilité et la performance de la plateforme. L'intégration de Brevo pour la gestion des contacts et l'envoi d'emails a été renforcée.

### Évolutions fonctionnelles

- Ajout d'une alerte CROUS sur la page d'accueil [#9d70e10](https://github.com/betagouv/monlogementetudiant/commit/9d70e10).
- Possibilité de cliquer sur l'icône du propriétaire pour accéder à son URL si disponible [#2190513](https://github.com/betagouv/monlogementetudiant/commit/2190513).
- Désactivation de l'autoconnexion pour les étudiants et affichage d'un message générique lors de l'inscription [#3c8a529](https://github.com/betagouv/monlogementetudiant/commit/3c8a529).
- Envoi d'un email de bienvenue aux propriétaires lors de leur création, au lieu d'un lien magique [#8c9cef7](https://github.com/betagouv/monlogementetudiant/commit/8c9cef7).
- Ajout d'un lien direct vers la FAQ des propriétaires sur Crisp Helpdesk [#a88a848](https://github.com/betagouv/monlogementetudiant/commit/a88a848).
- Ajout d'indicateurs clés de performance (KPI) pour le nombre total d'appartements par propriétaire dans l'administration [#bf83abc](https://github.com/betagouv/monlogementetudiant/commit/bf83abc).
- Ajout de statistiques intégrées sur les logements et les appartements, regroupés par CROUS et autres [#3d66bf2](https://github.com/betagouv/monlogementetudiant/commit/3d66bf2).
- Ajout d'aides à la mobilité CROUS [#87edc53](https://github.com/betagouv/monlogementetudiant/commit/87edc53).
- Pagination avec ellipses [#255ffbd](https://github.com/betagouv/monlogementetudiant/commit/255ffbd).
- Ajout de la diffusion et des RSJA FJT [#60930fa](https://github.com/betagouv/monlogementetudiant/commit/60930fa).
- Gestion des images dans S3 avec audit [#93608f8](https://github.com/betagouv/monlogementetudiant/commit/93608f8).

### Évolutions techniques

- Mise à jour de l'import d'Arpej avec un type de résidence typé au lieu d'une chaîne de caractères littérale [#186f282](https://github.com/betagouv/monlogementetudiant/commit/186f282).
- Priorisation du nom de la ville par rapport au code postal seul dans la fonction `ensureCity` [#1b0052d](https://github.com/betagouv/monlogementetudiant/commit/1b0052d) et [#2af6ae4](https://github.com/betagouv/monlogementetudiant/commit/2af6ae4).
- Intégration de Brevo pour l'envoi de contacts lors de la création de nouveaux utilisateurs ou de la mise à jour des logements [#010c052](https://github.com/betagouv/monlogementetudiant/commit/010c052).
- Ajout de l'attribut Brevo lors de la création d'un propriétaire [#5da25d8](https://github.com/betagouv/monlogementetudiant/commit/5da25d8).
- Possibilité de réinitialiser le mot de passe d'un étudiant depuis l'administration et envoi d'un email [#f7633b5](https://github.com/betagouv/monlogementetudiant/commit/f7633b5).
- Amélioration de la gestion des logements non CROUS avec la prise en compte de la disponibilité [#43f45c4](https://github.com/betagouv/monlogementetudiant/commit/43f45c4).

### Autres changements

- Mise à jour de la formulation de la section "hero" [#3910ef9](https://github.com/betagouv/monlogementetudiant/commit/3910ef9).
- Correction de fautes de frappe dans l'interface [#5eb2922](https://github.com/betagouv/monlogementetudiant/commit/5eb2922) et [#7472464](https://github.com/betagouv/monlogementetudiant/commit/7472464).
- Correction de bugs et amélioration de l'UX des badges de Différents Financeurs (DF) [#2bf469a](https://github.com/betagouv/monlogementetudiant/commit/2bf469a) et [#9805090](https://github.com/betagouv/monlogementetudiant/commit/9805090).
- Suppression de 'lyceen' du calculateur Locapass et modification des formulations [#2bf469a](https://github.com/betagouv/monlogementetudiant/commit/2bf469a).
- Mise à jour des badges UX sur les résultats de recherche et les détails du logement [#92f64c5](https://github.com/betagouv/monlogementetudiant/commit/92f64c5).
- Mise à jour de la configuration de Claude pour l'autofix des PR [#f8c5d3e](https://github.com/betagouv/monlogementetudiant/commit/f8c5d3e).
- Correction de bugs E2E [#31648f3](https://github.com/betagouv/monlogementetudiant/commit/31648f3).
- Correction du lien magique pour les propriétaires [#531ef07](https://github.com/betagouv/monlogementetudiant/commit/531ef07).
- Correction de l'adresse d'envoi des emails (no-reply) [#764bb38](https://github.com/betagouv/monlogementetudiant/commit/764bb38).
- Correction du préfixe du bucket S3 [#6c86a39](https://github.com/betagouv/monlogementetudiant/commit/6c86a39).
