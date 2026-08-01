## Changelog : apistration (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la sécurité et de la gestion des accès, notamment pour les éditeurs d'API. Des corrections et des améliorations ont également été apportées à la documentation, aux API et à l'expérience utilisateur, en particulier concernant les informations sur les API DGFIP et CNOUS. Plusieurs mises à jour de dépendances ont été effectuées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- **Gestion des éditeurs :** Amélioration significative de la gestion des éditeurs, incluant la création, la révocation et la prolongation de tokens d'accès. Les éditeurs peuvent désormais gérer leurs propres clés API via une interface dédiée. [#294](https://github.com/datagouv/apistration/pull/294)
- **API DGFIP :** Clarification de la documentation et ajout d'informations sur le numéro de TVA pour l'endpoint `numero_tva`. [#306](https://github.com/datagouv/apistration/pull/306)
- **API CNOUS :** Ajout de la prise en charge de l'INE (identifiant national étudiant) pour l'API CNOUS v5, avec des mocks pour les tests.  Ajout de la gestion des cas "boursier N-1" et "boursier N-2". [#292](https://github.com/datagouv/apistration/pull/292), [#270](https://github.com/datagouv/apistration/pull/270)
- **Démarche numérique :** Ajout d'un webhook pour l'API Particulier Démarche Numérique. [#266](https://github.com/datagouv/apistration/pull/266)
- **Accessibilité :** Améliorations de l'accessibilité, notamment des corrections pour les lecteurs d'écran et la navigation au clavier. [#241](https://github.com/datagouv/apistration/pull/241)
- **Statuts des demandes d'habilitation :** Tous les statuts des demandes d'habilitation sont désormais visibles. [#241](https://github.com/datagouv/apistration/pull/241)

### Évolutions techniques
- **Sécurité :** Renforcement de la sécurité en validant les adresses IP autorisées pour les tokens d'éditeur au moment de leur création. [#308](https://github.com/datagouv/apistration/pull/308)
- **Gestion des erreurs :** Ajout d'une nouvelle erreur (00213) pour les problèmes de correspondance de SIRET. [#249](https://github.com/datagouv/apistration/pull/249)
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans la gestion des tokens d'éditeur.
- **Dépendances :** Mise à jour de nombreuses dépendances (Ruby, Rails, Faraday, etc.) pour corriger des vulnérabilités et bénéficier des dernières améliorations.
- **CI/CD :** Amélioration du workflow de déploiement pour l'environnement de staging. [#273](https://github.com/datagouv/apistration/pull/273)
- **Documentation :** Génération automatique de la documentation OpenAPI avec les dernières modifications.

### Autres changements
- **Documentation :** Amélioration de la documentation pour les API FranceConnect et les intégrations d'éditeur.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la qualité du code.
- **Configuration :** Mise à jour de la configuration pour refléter les changements apportés à la plateforme.
- **Tests :** Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- **Mise à jour des mocks :** Régénération des mocks pour les API et correction de certaines erreurs.
- **Suppression de l'annonce changelog de l'intégration éditeur.** [#252](https://github.com/datagouv/apistration/pull/252)
- **Ajout d'un fichier `.personal` au `.gitignore`.** [#284](https://github.com/datagouv/apistration/pull/284)
- **Correction de l'INE erroné.** [#262](https://github.com/datagouv/apistration/pull/262)
- **Mise à jour de la date de changement d'année pour la deuxième année du secondaire.** [#247](https://github.com/datagouv/apistration/pull/247)
- **Suppression de l'annonce "bourses bientôt disponibles" sur le statut étudiant.** [#247](https://github.com/datagouv/apistration/pull/247)
- **Correction du nom de la page des paramètres de l'éditeur.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Correction de la documentation de l'éditeur.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Correction des liens de la documentation de l'éditeur.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Normalisation du type de déploiement de l'éditeur.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Validation des IP autorisées de l'éditeur à la source.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Initialisation des éditeurs avec les API qu'ils gèrent.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Pré-remplissage d'un token d'éditeur généré avec les IP autorisées de l'éditeur.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Suppression du bouton de copie sur les identifiants de délégation de l'éditeur.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Clarification du chevauchement des listes d'habilitations et de délégations de l'éditeur.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Extension de la documentation d'intégration de l'éditeur avec une introduction à la délégation et un espace éditeur.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Contrainte des IP du token de l'éditeur à la plage d'IP déclarée par l'éditeur.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Ajout d'une page de paramètres de l'éditeur reflétant l'édition admin, moins les champs verrouillés.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Explication des onglets habilitations et délégations dans l'espace éditeur.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Déplacement des liens de documentation/swagger de l'éditeur de l'en-tête vers la page des tokens.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Pointage des liens Documentation/Swagger de l'en-tête de l'éditeur vers les ressources de délégation.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Suppression de la colonne des scopes de la liste des délégations de l'éditeur.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Ajout d'une page Redoc /editeur/openapi pour le swagger de l'API de l'éditeur.** [#293](https://github.com/datagouv/apistration/pull/293)
- **Simplification de la phrase d'introduction de la liste des habilitations de l'éditeur.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Clarification du concept de délégation de l'éditeur dans le tableau.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Renommage des onglets de navigation de l'éditeur pour indiquer clairement à quelle ressource chacun appartient.** [#288](https://github.com/datagouv/apistration/pull/288)
- **Correction de la date du bureau ouvert.** [#305](https://github.com/datagouv/apistration/pull/305)
- **Correction d'une vulnérabilité ActiveStorage.** [#312](https://github.com/datagouv/apistration/pull/312)
