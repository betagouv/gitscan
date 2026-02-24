## Changelog : bhasile (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Bhasile au cours des 30 derniers jours. Les principales évolutions concernent la gestion des CPOM (Conventions de Partenariat Opérationnel et de Mutualisation) avec l'ajout de formulaires, de listes et de fonctionnalités de gestion des fichiers associés. Des améliorations ont également été apportées à la gestion des finances, à l'interface utilisateur et à la sécurité. Enfin, le nom de l'application a été mis à jour de "Place d'asile" à "Bhasile".

### Évolutions fonctionnelles
- Ajout de formulaires pour la création et la modification des CPOM (#947, #978, #981).
- Affichage des CPOM sur la page de la structure (#990).
- Ajout d'une liste des CPOM (#988).
- Possibilité d'ajouter des fichiers (conventions) aux CPOM (#972).
- Ajout de liens vers les CPOM dans le menu et l'en-tête (#996).
- Affichage des tableaux financiers sur la page de la structure (#971).
- Amélioration de la gestion des adresses (#1001).
- Correction d'un bug empêchant la définition du public à "Tout public" lors des modifications (#1020).
- Autorisation de valeurs négatives pour certains champs financiers (#1015, #1023).
- Correction d'un bug lié au crash des activités (#1008).
- Correction d'un bug de redirection après la déconnexion (#1003).
- Ajout d'un email de contact sur la page d'erreur 403 (#1009).
- Ajout de suivi sur la sélection de la carte (#998).
- Suppression des années du CPOM (#953).
- Ajout d'indicateurs de conformité (#944).
- Correction d'un bug lié aux liens de redirection dans les marqueurs de carte (#993).
- Correction d'un bug lié aux retours du formulaire CPOM (#992, #995).

### Évolutions techniques
- Mise à jour de la configuration Next.js (#975).
- Amélioration de la gestion des brackets et formatage du code avec ESLint et Prettier (#1011).
- Amélioration des contrôles de bloc (#1005).
- Ajout de restrictions sur les utilisateurs autorisés (#950).
- Suppression de TODOs (#1010).
- Mise à jour de jsdom et d'autres dépendances (#1007, #1006, #985, #960, #951).
- Suppression de fichiers inutiles dans le workflow CI/CD (#923).
- Ajout de documentation sur l'architecture backend (#999).
- Renommage de "demarches simplifiées" en "demarches numeriques" (#965).
- Suppression des champs "places à créer" et "fermer" (#946).
- Correction d'un problème de cohérence entre le département et le DNA (#966).
- Ajout d'un message de chargement pour l'utilisation (#962).
- Mise à jour du nom du projet de "Place d'Asile" à "Bhasile" (#982).
- Correction d'un problème de sécurité lié à la construction de commandes shell à partir de variables d'environnement (#949).

### Autres changements
- Ajout de tests e2e pour les formulaires de modification et de CPOM (#1019, #936, #984).
- Inversion des numéros de téléphone (#997).
- Ajout de couleurs d'arrière-plan aux titres dans le formulaire de finance (#967).
- Correction de fautes de frappe dans les finances (#969).
- Augmentation de la limite d'upload de fichiers à 30Mo (#958).
- Nettoyage du code après la gestion des CPOM (#819).
- Suppression des logs (#956).
- Ajout de la possibilité d'uploader des fichiers Excel avec macros (.xlsm) (#945).
- Autorisation de valeurs négatives pour les affectations de réserves de fonds dédiés (#4ff2ae6).
