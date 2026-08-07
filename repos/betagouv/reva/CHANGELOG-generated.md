## Changelog : reva (30 derniers jours, au 06 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans la gestion fine des droits d'accès, notamment pour les cohortes collectives. Le parcours de faisabilité dématérialisée a été considérablement enrichi pour les candidats, et la sécurité de l'API a fait l'objet d'une refonte majeure pour garantir un contrôle des données plus robuste et cohérent.

### Évolutions fonctionnelles
- **Gestion des VAE Collectives** : Introduction de permissions granulaires permettant de gérer précisément les droits de voir, modifier, supprimer une cohorte ou consulter les statistiques.
- **Parcours Candidat** :
    - Amélioration de la gestion des certificateurs : possibilité de choisir parmi plusieurs certificateurs, ajout de pages d'avertissement et mise à jour simplifiée des informations de contact.
    - Optimisation de la faisabilité dématérialisée : pré-sélection automatique du certificateur dans les documents PDF et amélioration de l'interface de saisie des compétences.
    - Amélioration de l'ergonomie des formulaires d'adresse (validation du code postal) et des tableaux de bord.
- **Administration** :
    - Nouveaux outils de sélection pour les formacodes et le périmètre d'accompagnement (version 2).
    - Meilleure visibilité des certificateurs "France Compétences" dans le backoffice.
    - Amélioration des capacités de recherche et de filtrage des candidatures.
- **Support et Contact** : Centralisation de l'aide utilisateur via la redirection de tous les liens de contact vers le centre d'aide Crisp.

### Évolutions techniques
- **Sécurité et Autorisation** : Refonte profonde de l'API avec la migration de la quasi-totalité des résolveurs (candidatures, rendez-vous, référentiels, finances, etc.) vers un nouveau moteur de politiques (`withPolicies`). Ce système permet une gestion des droits beaucoup plus fine et centralisée.
- **Infrastructure** : Correction des problèmes de timeout lors du démarrage des services sur Scalingo via une configuration optimisée de l'hostname.
- **Qualité logicielle** : 
    - Augmentation massive de la couverture de tests, incluant des tests de bout en bout pour les parcours de faisabilité et des tests HTTP rigoureux pour l'interopérabilité.
    - Centralisation et harmonisation des messages d'erreur de l'API pour une meilleure maintenance.
- **Performance** : Optimisation de la gestion du cache lors de la sélection des certificateurs et amélioration de la rapidité de rafraîchissement des données de certification.

### Autres changements
- **Expérience Développeur (DX)** : Ajout d'un script spécifique pour résoudre les erreurs de "chemins trop longs" sur Windows lors de l'utilisation de Turbopack.
- **Documentation** : Mise à jour des CGU sur le site web pour pointer vers le nouveau formulaire de contact.
- **Nettoyage** : Suppression de paramètres et de modèles de données obsolètes dans l'API.
