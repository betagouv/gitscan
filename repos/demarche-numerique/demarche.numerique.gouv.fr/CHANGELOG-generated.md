## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes en matière de fiabilité et d'outils d'administration. Les évolutions majeures concernent une meilleure gestion des interruptions de services externes (comme le RNF ou l'API Entreprise) grâce à un nouveau système de "mise en attente" des tâches, ainsi qu'une intégration renforcée de Brevo pour l'envoi d'emails. Pour les agents, de nouveaux outils facilitent la gestion des dossiers (demandes de compléments, propositions de pré-remplissage) et la gestion des accès (jetons API, gestion des instructeurs).

### Évolutions fonctionnelles

**Gestion des dossiers et instruction**
- Mise en place de la "Demande de complément" : les instructeurs peuvent désormais demander des informations supplémentaires à l'usager avec un motif précis [#14266].
- Amélioration du pré-remplissage : les instructeurs peuvent proposer des modifications de données directement aux usagers pour faciliter la correction des dossiers [#14313, #14287].
- Sécurisation de l'archivage : ajout de fenêtres de confirmation (modales) pour prévenir les erreurs d'archivage de dossiers en masse [#14181, #14266].
- Ajout de la traçabilité des décisions : intégration d'un tag indiquant la date et l'heure d'une décision [#14311].

**Gestion des utilisateurs et des experts**
- Autonomie des usagers : possibilité pour un utilisateur connecté de modifier son mot de passe depuis son profil [#13782].
- Clarté sur la suppression des comptes : amélioration des notifications expliquant ce qu'il advient des brouillons lors de la suppression d'un compte inactif [#14393].
- Suivi des experts : affichage du nombre d'avis donnés par un expert et notification automatique des autres experts lors de la publication d'un avis non confidentiel [#14415, #14429].

**Administration et outils de gestion**
- Optimisation des jetons API (API Tokens) : nouvelle interface permettant de dupliquer des jetons, de visualiser leur expiration et une sélection plus intuitive des procédures liées [#14425, #14405].
- Pilotage de l'API Entreprise : création d'un tableau de bord pour les gestionnaires afin de suivre l'état de santé des services externes [#14383].
- Gestion des instructeurs : possibilité de restreindre l'ajout d'instructeurs à un domaine d'email spécifique pour une meilleure sécurité des procédures [#14129, #14411].

**Expérience utilisateur**
- Transparence sur les services : affichage d'un état "dégradé" pour l'usager et l'instructeur lorsque les données externes (RNF) ne sont pas disponibles, évitant ainsi toute confusion [#14384, #14387].
- Corrections d'affichage : amélioration de l'ergonomie sur mobile, notamment pour les liens de messagerie [#14443].

### Évolutions techniques

**Fiabilité et résilience des services**
- Intégration de Brevo : migration vers l'API transactionnelle de Brevo pour l'envoi d'emails, incluant une gestion robuste des webhooks et un reporting des erreurs vers Sentry [#14470, #14432, #14111].
- Mécanisme de "Parking" : pour éviter l'encombrement des files d'attente lors de pannes de services tiers (API Entreprise), les tâches sont désormais mises en attente et réessayées périodiquement plutôt que de saturer le système [#14400, #14371].
- Résilience RNF : amélioration de la gestion des données dégradées du Référentiel National des Entreprises avec des cycles de réessai automatiques [#14384].

**Performance et Architecture**
- Mise à jour technologique : migration vers Ruby 4.0.9 [#14394].
- Optimisation des exports : passage à `zip_kit` pour la génération des archives de dossiers, améliorant la gestion de la mémoire et la rapidité de téléchargement [#14371].
- Sécurité des jetons : passage à un hachage SHA-256 pour l'authentification des jetons API [#14368].
- Optimisation des recherches : amélioration des performances sur la recherche d'utilisateurs et l'assignation des dossiers via l'ajout d'index en base de données [#14273, #14286].
- Refactorisation de l'authentification ProConnect pour une meilleure gestion des sessions et du MFA [#14385, #14314].

**Maintenance de la donnée**
- Migration des types de champs : conversion des anciens types de champs "nombre" vers les formats standards integer ou decimal [#14332, #14348].
- Nettoyage du code : suppression des anciens types de champs "cojo" et des fonctionnalités obsolètes [#14202].

### Autres changements
- Documentation : mise à jour de la documentation pour les administrateurs, incluant un lien vers les notes de version [#14292].
- Sécurité CI/CD : mise en place d'une vérification systématique de la signature GPG des commits lors des Pull Requests [#14417].
- Nettoyage : suppression de plusieurs drapeaux de fonctionnalités (feature flags) devenus inutiles [#14363, #14364, #14350].
