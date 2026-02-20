## Changelog : bhasile (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Bhasile (anciennement Place d'asile) au cours des 30 derniers jours. Les principales évolutions concernent l'ajout et l'amélioration de la gestion des CPOM (Convention de Partenariat Opérationnel et de Mutualisation), des corrections de bugs et des améliorations de l'interface utilisateur, notamment au niveau des formulaires financiers et de la gestion des structures.  L'outil a également été renommé en Bhasile.

### Évolutions fonctionnelles
- Ajout de la gestion des CPOM : ajout de liens, de formulaires, de listes et de la possibilité de joindre des fichiers liés aux CPOM (#947, #988, #990, #972, #978, #984, #992, #995).
- Amélioration de la gestion des structures : affichage des budgets avant la création de la structure (#1016), interdiction des valeurs négatives pour certains champs financiers (#1015, #1017), ajout d'informations CPOM sur la page structure (#959).
- Amélioration de l'interface utilisateur :
    - Ajout d'une adresse email de contact sur la page d'erreur 403 (#1009).
    - Amélioration du bloc "Activités" (#1004, #1008, #938).
    - Ajustement de la taille du logo dans différents contextes (#1002).
    - Ajout de suivi de la sélection de la carte (#998).
    - Correction d'un bug de redirection après déconnexion (#1003).
    - Renommage de "Places à créer et fermer" (#946).
- Ajout d'indicateurs de conformité (#944).
- Ajout d'un cron pour l'EIG (#937).
- Correction d'un bug empêchant la validation des structures subventionnées (#941).
- Correction d'un bug lié à la case à cocher "Pas d'évaluation" (#929).

### Évolutions techniques
- Renommage du projet de "Place d'Asile" à "Bhasile" (#982).
- Mise à jour de la configuration Next.js (#975).
- Amélioration de la sécurité : correction d'une vulnérabilité potentielle liée à la construction de commandes shell à partir de variables d'environnement (#949).
- Ajout de documentation sur l'architecture backend (#999).
- Ajout de restrictions sur les utilisateurs autorisés (#950).
- Ajout de tests E2E pour le formulaire CPOM (#984).
- Amélioration de la gestion des erreurs et des validations de formulaires (#981, #939, #940).
- Suppression de TODOs (#1010).
- Suppression de code inutile (#819).
- Ajout de brackets obligatoires et formatage du code avec Prettier (#1011).

### Autres changements
- Correction d'un bug où le public était remis à "Tout public" à chaque modification (#1020).
- Correction d'un bug lié à la liste des adresses (#1001).
- Correction d'un bug lié à la perte du département dans le formulaire (#983).
- Correction de typos dans les finances (#969).
- Mise à jour de plusieurs dépendances (jsdom, divers paquets mineurs) (#1006, #1007, #985, #960, #935).
- Exclusion de certains fichiers des vérifications (#923).
- Ajout d'un message de chargement pour l'utilisation (#962).
- Ajout de la possibilité d'uploader des fichiers Excel avec macros (.xlsm) (#945, #952).
- Suppression des années du CPOM (#964).
- Ajout de couleurs d'arrière-plan aux titres dans le formulaire de finance (#967).
- Ajout d'une incohérence entre le département et le DNA (#966).
- Suppression de logs (#956).
- Suppression de l'affichage du total dans les activités (#959).
- Mise à jour des mots utilisés dans le bouton de finalisation (#940).
