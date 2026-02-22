## Changelog : bhasile (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours de développement sur Bhasile (anciennement Place d'asile), l'outil de gestion du parc de logements pour demandeurs d’asile. Les améliorations portent principalement sur la gestion des CPOM (Conventions de Partenariat Opérationnel et de Mutualisation), les finances, et l'expérience utilisateur, avec des corrections de bugs et l'ajout de nouvelles fonctionnalités pour faciliter la saisie et le suivi des données.

### Évolutions fonctionnelles
- Ajout de la possibilité d'accepter des valeurs négatives pour le résultat net cumulé (#1023).
- Masquage des types de places avant la date de création (#1021).
- Correction d'un bug où le public était systématiquement mis à "Tout public" lors de chaque modification (#1020).
- Interdiction des valeurs négatives pour le nombre de places (#1017).
- Masquage des années de budget avant la création de la structure (#1016).
- Interdiction des valeurs négatives pour la plupart des champs financiers (#1015).
- Ajout d'une adresse email de contact sur la page d'erreur 403 (#1009).
- Ajout de liens vers les CPOM dans le menu et l'en-tête (#996).
- Affichage des CPOM sur la page de la structure (#990).
- Ajout de la possibilité de rendre optionnel le "Total Produit Proposé" pour les années 2021, 2022 et 2023 (#989).
- Ajout de la gestion des fichiers de convention (CPOM) (#972).
- Ajout d'un modal de confirmation pour les CPOM (#978).
- Ajout du formulaire de création de CPOM (#947).
- Correction d'un bug empêchant la suppression de dates dans les CPOM (#942).
- Ajout d'indicateurs de conformité v2 (#944).
- Correction de la validation sur les structures subventionnées (#941).
- Ajout de la possibilité d'uploader des fichiers Excel avec macros (.xlsm) (#945).
- Correction d'un bug de redirection sur les marqueurs de la carte (#993).
- Correction d'un bug sur la page d'activité (#1008, #938).
- Correction d'un bug de déconnexion (#1003).
- Amélioration de l'affichage des tableaux financiers (#971, #980).
- Ajout de tests E2E pour le formulaire de modification (#1019) et le formulaire CPOM (#984).

### Évolutions techniques
- Mise à jour de ESLint pour forcer l'utilisation de parenthèses obligatoires (#1011).
- Amélioration du bloc de contrôle (#1005).
- Ajout de restrictions sur les utilisateurs autorisés (#950).
- Mise à jour de Next.js (vers 16.1.5) (#951, #985, #960).
- Mise à jour de jsdom (vers 28.0.0) (#1007).
- Suppression de TODOs (#1010).
- Suppression de code obsolète lié aux places à créer et fermer (#946).
- Suppression de logs inutiles (#956).
- Mise à jour de la configuration Next.js (#975).
- Ajout de documentation sur l'architecture backend (#999).
- Correction d'un problème potentiel de sécurité lié à l'exécution de commandes shell (#949).
- Suppression des années dans les CPOM (#953).
- Ajout d'un message de chargement pour l'utilisation (#962).

### Autres changements
- Renommage de "Place d'Asile" en "Bhasile" (#982).
- Inversion des numéros de téléphone (#997).
- Correction de fautes de frappe dans les finances (#969).
- Ajout d'un incohérence entre département et ADN (#966).
- Suppression de fichiers inutiles des vérifications (#923).
- Ajustement de la taille du logo (#1002).
- Ajout de suivi de la sélection sur la carte (#998).
- Mise à jour du wording du bouton de finalisation (#940).
- Augmentation de la limite d'upload de fichiers à 30Mo (#958).
- Nettoyage du code post-CPOM (#819).
