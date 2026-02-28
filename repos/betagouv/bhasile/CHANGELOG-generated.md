## Changelog : bhasile (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de Bhasile (anciennement Place d'Asile), l'outil de gestion du parc de logements pour demandeurs d’asile. Les dernières mises à jour se concentrent sur l'ajout et l'amélioration de la gestion des CPOM (Conventions de Partenariat Opérationnel et de Mutualisation), avec l'ajout de formulaires, de listes, de liens et de tests associés. Des améliorations ont également été apportées à la gestion des finances, à l'interface utilisateur et à la sécurité.

### Évolutions fonctionnelles
- Ajout de la gestion des CPOM : formulaires, listes, liens dans le menu et l'en-tête (#947, #972, #988, #996).
- Ajout d'un modal de confirmation pour les CPOM (#978).
- Affichage des CPOM sur la page structure (#990).
- Amélioration de l'affichage des tableaux financiers (#991).
- Possibilité d'accepter des résultats nets cumulés négatifs (#1023).
- Correction de l'affichage de l'année du CPOM dans les documents financiers (#1032).
- Correction de l'affichage des typologies d'années manquantes dans les formulaires opérateur et agentf (#1030).
- Correction d'un bug où le public était toujours mis à "Tout public" lors des modifications (#1020).
- Interdiction des valeurs négatives pour la plupart des champs financiers (#1015) et pour le nombre de places (#1017).
- Ajout d'un journal d'audit (#1018).
- Modification de la page 403 pour afficher un email de contact (#1009).
- Correction d'un bug de redirection des marqueurs sur la carte (#993).
- Ajout d'indicateurs financiers (#957).
- Amélioration de l'affichage des adresses (#1001).

### Évolutions techniques
- Renommage de "Place d'Asile" en "Bhasile" dans le code et l'interface (#982).
- Mise à jour de la configuration Next.js (#975).
- Refactorisation des uploads de fichiers (#994).
- Ajout de restrictions sur les utilisateurs autorisés (#950).
- Amélioration des contrôles de bloc (#1005).
- Ajout de tests E2E pour les formulaires de modification et CPOM (#1019, #984).
- Correction d'un crash des activités (#1008).
- Ajout de documentation sur l'architecture backend (#999).
- Mise à jour des dépendances (jsdom, divers paquets mineurs et correctifs) (#1007, #1024, #985, #960).
- Ajout de règles ESLint et formatage avec Prettier (#1011).
- Suppression de TODOs (#1010).
- Suppression de code inutile et nettoyage du code (#963, #923, #819).

### Autres changements
- Correction de fautes de frappe dans les finances (#969).
- Incohérence entre département et code DNA corrigée (#966).
- Message de chargement amélioré pour l'utilisation (#962).
- Suppression des années des CPOM (temporairement réintégrées ensuite) (#964, #953).
- Suppression de logs inutiles (#956).
- Ajustement de la taille du logo (#1002).
- Ajout de tracking sur la sélection de la carte (#998).
- Ajout de couleurs d'arrière-plan aux titres dans le formulaire financier (#967).
- Correction d'un bug empêchant le bon fonctionnement du formulaire CPOM (#979, #981).
- Correction d'un bug empêchant l'envoi des données du formulaire de modification des finances (#87581dd).
- Correction d'un bug où le département était réinitialisé à chaque montage de formulaire (#983).
- Ajout de la possibilité d'affecter des réserves de fonds dédiés négatives (#4ff2ae6).
- Mise à jour des données de test pour 2026 (#1031).
- Correction d'un bug lié à la récupération des structures (#971).
- Correction d'un bug empêchant l'affichage correct des structures (#980).
